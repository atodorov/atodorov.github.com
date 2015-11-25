---
layout: post
Title: How Large Are My MySQL Tables
date: 2013-02-20 12:03
comments: true
Tags: MySQL, Amazon, S3
---

<img src="/images/database.jpg" alt="database" style="display:block;clear:both;"/>
Image CC-BY-SA, [Michael Mandiberg](http://www.flickr.com/photos/theredproject/3332644561/)

I found two good blog posts about investigating MySQL internals: 
[Researching your MySQL table sizes](http://www.mysqlperformanceblog.com/2008/03/17/researching-your-mysql-table-sizes/) and
[Finding out largest tables on MySQL Server](http://www.mysqlperformanceblog.com/2008/02/04/finding-out-largest-tables-on-mysql-server/).
Using the queries against my site [Difio](http://www.dif.io) showed:

    :::sql
    mysql> SELECT CONCAT(table_schema, '.', table_name),
        ->        CONCAT(ROUND(table_rows / 1000000, 2), 'M')                                    rows,
        ->        CONCAT(ROUND(data_length / ( 1024 * 1024 * 1024 ), 2), 'G')                    DATA,
        ->        CONCAT(ROUND(index_length / ( 1024 * 1024 * 1024 ), 2), 'G')                   idx,
        ->        CONCAT(ROUND(( data_length + index_length ) / ( 1024 * 1024 * 1024 ), 2), 'G') total_size,
        ->        ROUND(index_length / data_length, 2)                                           idxfrac
        -> FROM   information_schema.TABLES
        -> ORDER  BY data_length + index_length DESC;
    +----------------------------------------+-------+-------+-------+------------+---------+
    | CONCAT(table_schema, '.', table_name)  | rows  | DATA  | idx   | total_size | idxfrac |
    +----------------------------------------+-------+-------+-------+------------+---------+
    | difio.difio_advisory                   | 0.04M | 3.17G | 0.00G | 3.17G      |    0.00 |
    +----------------------------------------+-------+-------+-------+------------+---------+

The table of interest is `difio_advisory` which had 5 `longtext` fields. Those fields were
not used for filtering or indexing the rest of the information.
They were just storage fields - a `nice' side effect of using Django's ORM.


I have migrated the data to Amazon S3 and stored it in JSON format there. After dropping these
fields the table was considerably smaller:

    :::sql
    +----------------------------------------+-------+-------+-------+------------+---------+
    | CONCAT(table_schema, '.', table_name)  | rows  | DATA  | idx   | total_size | idxfrac |
    +----------------------------------------+-------+-------+-------+------------+---------+
    | difio.difio_advisory                   | 0.01M | 0.00G | 0.00G | 0.00G      |    0.90 |
    +----------------------------------------+-------+-------+-------+------------+---------+


For those interested I'm using [django-storages](https://github.com/e-loue/django-storages)
on the back-end to save the data in S3 when generated. On the front-end I'm using
[dojo.xhrGet](http://dojotoolkit.com) to load the information directly into the browser.


I'd love to hear your feedback in the comments section below. Let me know 
what you found for your own databases. Were there any issues? How did you deal
with them? 
