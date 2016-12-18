Cheetah v1.0
==============

* [News](#news)
    * [Say Hello to Cheetah](#say-hello-to-cheetah)
* [Installation](#installation)
    * [How to run Cheetah ?](#how-to-run-cheetah-)
* [Future Steps](#future-steps)
    * [Dashboard for cheetah](#dashboard-for-cheetah)
  

## News
### Say Hello to Cheetah

`cheetah` is an AWS security audit tools for the ops engineers. Cheetah can audit the instance security rules (ACL or Security Groups) and could alert you if there is any security issue.

## Installation
### How to run Cheetah ?

To run Cheetah, only you should [create a profile](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) for your aws account and then run it from your command line.

``` python manage.py --profile your_profile_name ```

and then browse to

``` http://localhost:5000/ec2/list ```

That's works!

## Future Steps
### Dashboard for Cheetah

We are planning to create a dashboard for Cheetah to preview statistics and security charts .
