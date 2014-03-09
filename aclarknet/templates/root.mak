<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../assets/ico/favicon.ico">

    <%block name="title">
        <title>ACLARK.NET, LLC &mdash; Home</title>
    </%block>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">

    <!-- Custom styles for this template -->
    <link href="/static/justified-nav.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

    <style type="text/css">
      body {
        background: url(http://ec944bcf33b48b690862-191a9659b8fb7703d8bd848e1f8d96be.r38.cf1.rackcdn.com/IMG_0256.JPG) center top no-repeat #24261A;
      }
      .row {
        background: #f9f9f9;
        padding: 1em;
      }
      <%block name="style">
      </%block>


    </style>

    <link href="/static/font-awesome.css" rel="stylesheet">


  </head>

  <body>

    <div class="container">

      <div class="masthead">
        <h3 class="text-muted"><a href="/">ACLARK.NET, LLC</a></h3>
        <ul class="nav nav-justified">
          <%block name="nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="/clients">Clients</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/team">Team</a></li>
            <li><a href="/testimonials">Testimonials</a></li>
            <li><a href="/contact">Contact</a></li>
          </%block>
        </ul>
      </div>

      <!-- Jumbotron -->
      <%block name="jumbotron">
      <div class="jumbotron">
        <h1>We know Python.<br />We know open source.</h1>
        <p class="lead">Create professional web services for your business efficiently, effectively and economically with open source Python software.
        We&apos;ll show you how&hellip;</p>

        <a class="btn btn-large btn-success" href="/contact">Get started today</a>
      </div>

      <!-- Example row of columns -->
      <div class="row">
        <div class="col-lg-4">
          <h2>Team</h2>
          <p><i class="icon-group icon-2x pull-left"></i>Our team offers extensive experience in the development, deployment and maintenance of Python-based w
eb applications. Please review our services, team, and clients sections for a summary of our experience and qualifications.</p>
          <p><a class="btn btn-primary" href="#" role="button">View details &raquo;</a></p>
        </div>
        <div class="col-lg-4">
          <h2>Heading</h2>
          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
          <p><a class="btn btn-primary" href="#" role="button">View details &raquo;</a></p>
       </div>
        <div class="col-lg-4">
          <h2>Heading</h2>
          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa.</p>
          <p><a class="btn btn-primary" href="#" role="button">View details &raquo;</a></p>
        </div>
      </div>
      </%block>

      <!-- Site footer -->
      <div class="footer">

        <p class="pull-left">&copy; ACLARK.NET, LLC 2004-2014</p>

        <p class="pull-right" style="color: white">
            Made with <a href="http://twitter.github.io/bootstrap">Bootstrap</a> and <a href="http://pylonsproject.org">Pyramid</a>.
            Icons by <a href="http://fortawesome.github.io/Font-Awesome/">Font Awesome</a>.
            Photo by <a href="http://about.me/alex.clark">Alex Clark</a>.
        </p>

        <p style="text-align: center">

<a href="https://twitter.com/aclarknet" class="twitter-follow-button" data-show-count="false" data-size="large" data-dnt="true">Follow @aclarknet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);j
s.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>

        </p>

      </div>

    </div> <!-- /container -->

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
  </body>
</html>
