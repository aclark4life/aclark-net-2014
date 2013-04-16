<%inherit file="root.mak"/>

<%block name="title">
    <title>ACLARK.NET, LLC &mdash; Contact</title>
</%block>

<%block name="nav">
    <li><a href="/">Home</a></li>
    <li><a href="/clients">Clients</a></li>
    <li><a href="/services">Services</a></li>
    <li><a href="/team">Team</a></li>
    <li><a href="/testimonials">Testimonials</a></li>
    <li class="active"><a href="/contact">Contact</a></li>
</%block>

<%block name="jumbotron">
    <h1>Contact</h1>
    <h2>The best way to contact us is via the email address, phone number or website form below.</h2>
    <div class="row-fluid">
        <div class="span12">
            <p class="lead"><i class="icon-envelope icon-2x pull-left"></i><i class="icon-phone icon-2x pull-left"></i>The Python programming language and open source software in general provide tremendous opportunities to businesses, but often require an expert to take advantage of. We provide services that empower individuals and organizations to benefit from such opportunities, and we would love to help you! Please contact us to schedule a time to discuss your needs. We look forward to working with you.</p>
            <br />
            <br />
            <div style="text-align: left ; margin: auto; width: 740px;">
                <% error = request.session.pop_flash('errors') %>
                <% success = request.session.pop_flash() %>
                % if error:
                    <div class="alert alert-block alert-error">${error[0]}</div>
                % endif
                % if success:
                    <div class="alert alert-block alert-success">${success[0]}</div>
                % endif
                ${form|n}
            </div>
            <hr>
            <p class="contact">
                ACLARK.NET, LLC <br />
                Bethesda, MD USA <br />
                Email: <a href="mailto:info@aclark.net">info@aclark.net</a> <br />
                Phone: 301-312-5236
            </p>
            <!--
            <form action="/contact" method="POST">
                <p class="contact">
                    <input type="text" placeholder="Your email">
                    <textarea rows="3" placeholder="Your message"></textarea>
                    <input class="btn btn-block btn-large" type="submit" value="Send"> 
                </p>
            </form>
            -->
        </div>
    </div>
</%block>
