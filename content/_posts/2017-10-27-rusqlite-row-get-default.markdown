Title: Fallback to default values for NULL columns in Rust SQLite
date: 2017-10-27 16:12
comments: true
Tags: fedora.planet

I have been working on code which changed its DB schema to add a NULL column
without a default value! The standard `row.get()` from Rusqlite throws errors
because NULL is not a valid integer value.

The solution is to use `row.get_checked()` like so:

    :::rust
    let build_id = row.get_checked(3).unwrap_or(0);

Interestingly enough I wasn't able to find clear information about this on the
Internet so here it is.

Thanks for reading and happy hacking!
