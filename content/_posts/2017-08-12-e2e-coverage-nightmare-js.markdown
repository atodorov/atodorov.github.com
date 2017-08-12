Title: Code coverage from Nightmare.js tests
Headline: end-to-end testing of React application
date: 2017-08-12 18:11
comments: true
Tags: fedora.planet, QA
og_image: images/code_coverage_analysis.png
twitter_image: images/code_coverage_analysis.png

In this article I'm going to walk you through the steps required
to collect code coverage when running an end-to-end test suite
against a React.js application.

The application under test looks like this

    :::html
    <!doctype html>
    <html lang="en-us" class="layout-pf layout-pf-fixed">
      <head>
        <!-- js dependencies skipped -->
      </head>
      <body>
        <div id="main"></div>
        <script src="./dist/main.js?0ca4cedf3884d3943762"></script>
      </body>
    </html>

It is served as an `index.html` file and a `main.js` file which intercepts
all interactions from the user and sends requests to the backend API when
needed.

There is an existing unit-test suite which loads the individual components
and tests them in isolation.
[Apparently people do this](https://twitter.com/atodorov_/status/886881560754102272)!

There is also an end-to-end test suite which does the majority of the testing.
It fires up a browser instance and interacts with the application. Everything
runs inside Docker containers providing a full-blown production-like environment.
They look like this

    :::javascript
    test('should switch to Edit Recipe page - recipe creation success', (done) => {
      const nightmare = new Nightmare();
      nightmare
        .goto(recipesPage.url)
        .wait(recipesPage.btnCreateRecipe)
        .click(recipesPage.btnCreateRecipe)
        .wait(page => document.querySelector(page.dialogRootElement).style.display === 'block'
          , createRecipePage)
        .insert(createRecipePage.inputName, createRecipePage.varRecName)
        .insert(createRecipePage.inputDescription, createRecipePage.varRecDesc)
        .click(createRecipePage.btnSave)
        .wait(editRecipePage.componentListItemRootElement)
        .exists(editRecipePage.componentListItemRootElement)
        .end() // remove this!
        .then((element) => {
          expect(element).toBe(true);
          // here goes coverage collection helper
          done(); // remove this!
        });
    }, timeout);

The browser interaction is handled by Nightmare.js (sort of like Selenium) and
the test runner is Jest.


Code instrumentation
--------------------

The first thing we need is to instrument the application code to provide coverage
statistics. This is done via `babel-plugin-istanbul`. Because unit-tests are
executed a bit differently we want to enable conditional instrumentation. In reality
for unit tests we use `jest --coverage` which enables istanbul on the fly and having
the code already instrumented breaks this. So I have the following in `webpack.config.js`

    :::javascript
    if (process.argv.includes('--with-coverage')) {
      babelConfig.plugins.push('istanbul');
    }

and then build my application with `node run build --with-coverage`.

You can execute `node run start --with-coverage`, open the JavaScript console
in your browser and inspect the `window.__coverage__` variable. If this is defined
then the application is instrumented correctly.


Fetching coverage information from within the tests
---------------------------------------------------

Remember that `main.js` from the beginning of this post? It lives inside `index.html`
which means everything gets downloaded to the client side and executed there.
When running the end-to-end test suite that is the browser instance which is controlled
via Nightmare. **You have to pass `window.__coverage__` from the browser scope back to
nodejs scope via `nightmare.evaluate()`**! I opted to directly save the coverage data
on the file system and make it available to coverage reporting tools later!

My coverage collecting snippet looks like this

    :::javascript
    nightmare
      .evaluate(() => window.__coverage__) // this executes in browser scope
      .end() // terminate the Electron (browser) process
      .then((cov) => {
        // this executes in Node scope
        // handle the data passed back to us from browser scope
        const strCoverage = JSON.stringify(cov);
        const hash = require('crypto').createHmac('sha256', '')
          .update(strCoverage)
          .digest('hex');
        const fileName = `/tmp/coverage-${hash}.json`;
        require('fs').writeFileSync(fileName, strCoverage);
    
        done(); // the callback from the test
      })
    .catch(err => console.log(err));

Nightmare returns `window.__coverage__` from browser scope back to nodejs scope
and we save it under `/tmp` using a hash value of the coverage data as the file
name.

*Side note:* I do have about 40% less coverage files than number of test cases.
This means some test scenarios exercise the same code paths. Storing the individual
coverage reports under a hashed file name makes this very easy to see!

Note that in my coverage handling code I also call `.end()` which will terminate
the browser instance and also execute the `done()` callback which is being passed
as parameter to the test above! This is important because it means we had to update
the way tests were written. In particular the Nightmare method sequence doesn't
have to call `.end()` and `done()` except in the coverage handling code. The
coverage helper must be the last code executed inside the body of the last
`.then()` method. This is usually after all assertions (expectations) have been met!

Now this coverage helper needs to be part of every single test case so I
wanted it to be a one line function, easy to copy&paste! All my attempts to
move this code inside a module have been futile. I can get the module loaded
but it kept failing with
`Unhandled promise rejection (rejection id: 1): cov_23rlop1885 is not defined`;`

At the end I've resorted to this simple hack

    :::javascript
    eval(fs.readFileSync('utils/coverage.js').toString());

Shout-out to [Krasimir Tsonev](http://krasimirtsonev.com/) who joined me on a two
days pairing session to figure this stuff out. Too bad we couldn't quite figure it
out. If you do please send me a pull request!

Reporting the results
---------------------

All of these `coverage-*.json` files are directly consumable by `nyc` - the
coverage reporting tool that comes with the Istanbul suite! I mounted
`.nyc_output/` directly under `/tmp` inside my Docker container so I could

    nyc report
    nyc report --reporter=lcov | codecov

We can also modify the unit-test command to
`jest --coverage --coverageReporters json --coverageDirectory .nyc_output` so it
produces a `coverage-final.json` file for `nyc`. Use this if you want to combine
the coverage reports from both test suites.

Because I'm using Travis CI the two test suites are executed independently and
there is no easy way to share information between them. Instead I've switched
from Coveralls to CodeCov which is smart enough to merge coverage submissions
coming from multiple jobs on the same git commits. You can compare the commit
[submitting only unit-test results](https://codecov.io/gh/atodorov/welder-web/commit/46556808e42a21f48d008ced2d53ffe176c01b6d)
with the one
[submitting coverage from both test suites](https://codecov.io/gh/atodorov/welder-web/commit/15f437477c17b63797cdb2455f1371336d7dc0e5).


All of the above steps are put into practice in
[PR #136](https://github.com/weldr/welder-web/pull/136) if you want to check them out!

Thanks for reading and happy testing!
