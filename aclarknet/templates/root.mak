<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Template &middot; Bootstrap</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="http://twitter.github.io/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <link href="/static/aclarknet.css" rel="stylesheet">
    <link href="/static/font-awesome.css" rel="stylesheet">
    <style type="text/css">
      body {
        background: url(/static/IMG_0256.JPG) center top no-repeat; 
        padding-top: 20px;
        padding-bottom: 60px;
      }

      /* Custom container */
      .container {
        margin: 0 auto;
        max-width: 1000px;
      }
      .container > hr {
        margin: 60px 0;
      }

      /* Main marketing message and sign up button */
      .jumbotron {
        margin: 80px 0;
        text-align: center;
      }
      .jumbotron h1 {
        font-size: 99px;
        line-height: 1;
      }
      .jumbotron .lead {
        font-size: 24px;
        line-height: 1.25;
        margin-right: 85px;
      }
      .jumbotron .btn {
        font-size: 21px;
        padding: 14px 24px;
      }

      /* Supporting marketing content */
      .marketing {
        margin: 60px 0;
      }
      .marketing p + h4 {
        margin-top: 28px;
      }


      /* Customize the navbar links to be fill the entire space of the .navbar */
      .navbar .navbar-inner {
        padding: 0;
      }
      .navbar .nav {
        margin: 0;
        display: table;
        width: 100%;
      }
      .navbar .nav li {
        display: table-cell;
        width: 1%;
        float: none;
      }
      .navbar .nav li a {
        font-weight: bold;
        text-align: center;
        border-left: 1px solid rgba(255,255,255,.75);
        border-right: 1px solid rgba(0,0,0,.1);
      }
      .navbar .nav li:first-child a {
        border-left: 0;
        border-radius: 3px 0 0 3px;
      }
      .navbar .nav li:last-child a {
        border-right: 0;
        border-radius: 0 3px 3px 0;
      }
      .row-fluid {
        background: #f9f9f9;
        border-radius: 3px;
      }
      .span4, .span12 {
        padding: 14px 24px;
      }
      .footer {
        color: #f9f9f9;
      }
    </style>
    <link href="http://twitter.github.io/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://twitter.github.io/bootstrap/assets/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://twitter.github.io/bootstrap/assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://twitter.github.io/bootstrap/assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://twitter.github.io/bootstrap/assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="http://twitter.github.io/bootstrap/assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="http://twitter.github.io/bootstrap/assets/ico/favicon.png">
  </head>

  <body>

    <div class="container">

    <a href="https://github.com/ACLARKNET/aclarknet"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_gray_6d6d6d.png" alt="Fork me on GitHub"></a>

      <div class="masthead">

        <h3 class="muted"><a href="/">ACLARK.NET, LLC</a></h3>

        <div class="navbar">
          <div class="navbar-inner">
            <div class="container">
              <ul class="nav">
                <%block name="nav">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#">Projects</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Downloads</a></li>
                <li><a href="#">About</a></li>
                <li><a href="/contact">Contact</a></li>
                </%block>
              </ul>
            </div>
          </div>
        </div><!-- /.navbar -->
      </div>



      <!-- Jumbotron -->
      <%block name="jumbotron">
      <div class="jumbotron">
        <h1>We know Python.<br />We know open source.</h1>
        <p class="lead">Do you want to create professional web services for your business, on a budget? Use open source Python software for instant ROI, and more.</p>
        <a class="btn btn-large btn-success" href="/contact">Get started today</a>
      </div>
      </%block>


      <hr>

      <!-- Example row of columns -->
      <div class="row-fluid"> 
        <div class="span4"> 
          <h2>Our Team</h2>
          <p>Our team offers extensive experience in the development, deployment and maintenance of Python-based web applications. Please review our services, team, and clients sections for a summary of our experience and qualifications.</p>
          <p><a class="btn" href="/team">View details &raquo;</a></p>
        </div>
        <div class="span4">
          <h2>Our Location</h2>
          <p>We are located in Bethesda, MD: a suburb of Washington, DC USA. If you are in the area, please get in touch. If you are not in the area, please get in touch anyway; we service a global community of individuals and organizations and take pride in our ability to do so.</p>
          <p><a class="btn" href="/contact">View details &raquo;</a></p>
       </div>
        <div class="span4">
          <h2>Our Community</h2>
          <p>In 2008, we created a Maryland 501(c)(3) non-profit organization to expand our outreach and service to the Python community in Washington, DC USA. One of our most significant contributions via this organization is the hosting of Plone Conference 2008.</p>
          <p><a class="btn" href="http://dcpython.org">View details &raquo;</a></p>
        </div>
      </div>

      <hr>

      <div class="footer">
        <p>&copy; ACLARK.NET, LLC 2004-2013. All rights reserved.</p>
      </div>

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://twitter.github.io/bootstrap/assets/js/jquery.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-transition.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-alert.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-modal.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-dropdown.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-scrollspy.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-tab.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-tooltip.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-popover.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-button.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-collapse.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-carousel.js"></script>
    <script src="http://twitter.github.io/bootstrap/assets/js/bootstrap-typeahead.js"></script>

  </body>
</html>

