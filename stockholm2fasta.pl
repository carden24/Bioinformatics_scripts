
    

  

<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <script type="text/javascript">var NREUMQ=[];NREUMQ.push(["mark","firstbyte",new Date().getTime()]);</script>
        <title>perl/stockholm2fasta.pl at master from ihh/dart - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    
    

    <meta content="authenticity_token" name="csrf-param" />
<meta content="2e1b9efa608892dec046635b7eab90a702157c01" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/stylesheets/bundle_github.css?615dc4415914822f1692ffeb95691446f898bde0" media="screen" rel="stylesheet" type="text/css" />
    

    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/jquery/jquery-1.6.1.min.js" type="text/javascript"></script>
    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundle_github.js?a4fe0e1f0bd644e228e91244bd6c0c313a3bade4" type="text/javascript"></script>

    

    
  <link rel='permalink' href='/ihh/dart/blob/e1ff4d6b483bb64c89170c8babb9b4f75ec2a12c/perl/stockholm2fasta.pl'>

  <link href="https://github.com/ihh/dart/commits/master.atom" rel="alternate" title="Recent Commits to dart:master" type="application/atom+xml" />

    

    <meta name="description" content="dart - DNA, Amino Acid and RNA Tests" />
  

        <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3769691-2']);
      _gaq.push(['_setDomainName', 'none']);
      _gaq.push(['_trackPageview']);
      _gaq.push(['_trackPageLoadTime']);
      (function() {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>

  </head>

  

  <body class="logged_out page-blob windows env-production">
    

    

    

    <div class="subnavd" id="main">
      <div id="header" class="true">
          <a class="logo boring" href="https://github.com">
            
            <img alt="github" class="default" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6.png" />
            <!--[if (gt IE 8)|!(IE)]><!-->
            <img alt="github" class="hover" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6-hover.png" />
            <!--<![endif]-->
          </a>

        
        <div class="topsearch">
  
    <!--
      make sure to use fully qualified URLs here since this nav
      is used on error pages on other domains
    -->
    <ul class="nav logged_out">
      
      <li class="pricing"><a href="https://github.com/plans">Pricing and Signup</a></li>
      
      <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
      <li class="features"><a href="https://github.com/features">Features</a></li>
      
      <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      
      <li class="login"><a href="https://github.com/login?return_to=%2Fihh%2Fdart%2Fblob%2Fmaster%2Fperl%2Fstockholm2fasta.pl">Login</a></li>
    </ul>
  
</div>

      </div>

      
      
        
    <div class="site">
      <div class="pagehead repohead vis-public    instapaper_ignore readability-menu">

      
      <div id="entice">
        <div class="explanation">
          <h2><strong>ihh</strong> is using GitHub to share code with you!</h2>
        <p>
          GitHub is more than just a place to share code. It's a place to keep tabs on your favorite developers and projects, easily contribute fixes and new features, and visualize what's going on inside your codebase!
        </p>
        </div>
        <div class="signup">
          <a href="/signup/free?green&amp;referral_code=entice-banner" id="entice-signup-button">Sign Up Now</a>
          <p id="oss-caption">Free for open source</p>
        </div>
      </div>
      
    

      <div class="title-actions-bar">
        <h1>
          <a href="/ihh">ihh</a> /
          <strong><a href="/ihh/dart" class="js-current-repository">dart</a></strong>
          
          
        </h1>

        
    <ul class="actions">
      

      
        
        <li>
          
            <a href="/ihh/dart/toggle_watch" class="minibutton btn-watch watch-button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '2e1b9efa608892dec046635b7eab90a702157c01'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Watch</span></a>
          
        </li>
        
          
            <li><a href="/ihh/dart/fork" class="minibutton btn-fork fork-button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '2e1b9efa608892dec046635b7eab90a702157c01'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>
          

          
        
      
      
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers ">
            <a href="/ihh/dart/watchers" title="Watchers" class="tooltipped downwards">
              11
            </a>
          </li>
          <li class="forks">
            <a href="/ihh/dart/network" title="Forks" class="tooltipped downwards">
              4
            </a>
          </li>
        </ul>
      </li>
    </ul>

      </div>

        
  <ul class="tabs">
    <li><a href="/ihh/dart" class="selected" highlight="repo_source">Source</a></li>
    <li><a href="/ihh/dart/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/ihh/dart/network" highlight="repo_network">Network</a></li>
    <li><a href="/ihh/dart/pulls" highlight="repo_pulls">Pull Requests (0)</a></li>

    

    
      
      <li><a href="/ihh/dart/issues" highlight="issues">Issues (0)</a></li>
    

    
    <li><a href="/ihh/dart/graphs" highlight="repo_graphs">Graphs</a></li>

    

    <li class="contextswitch nochoices">
      <span class="repo-tree toggle leftwards"
            
            data-master-branch="master"
            data-ref="master">
        <em>Branch:</em>
        <code>master</code>
      </span>
    </li>
  </ul>

  <div style="display:none" id="pl-description"><p><em class="placeholder">click here to add a description</em></p></div>
  <div style="display:none" id="pl-homepage"><p><em class="placeholder">click here to add a homepage</em></p></div>

  <div class="subnav-bar">
  
  <ul>
    <li>
      <a href="/ihh/dart/branches" class="dropdown">Switch Branches (1)</a>
      <ul>
        
          
            <li><strong>master &#x2713;</strong></li>
            
      </ul>
    </li>
    <li>
      <a href="#" class="dropdown defunct">Switch Tags (0)</a>
      
    </li>
    <li>
    
    <a href="/ihh/dart/branches" class="manage">Branch List</a>
    
    </li>
  </ul>
</div>

  
  
  
  
  
  



        
    <div id="repo_details" class="metabox clearfix">
      <div id="repo_details_loader" class="metabox-loader" style="display:none">Sending Request&hellip;</div>

      
        <a href="/ihh/dart/downloads" class="download-source" data-facebox-url="/ihh/dart/archives/master" id="download_button" title="Download source, tagged packages and binaries."><span class="icon"></span>Downloads</a>
      

      <div id="repository_desc_wrapper">
      <div id="repository_description" rel="repository_description_edit">
        
          <p>DNA, Amino Acid and RNA Tests
            <span id="read_more" style="display:none">&mdash; <a href="#readme">Read more</a></span>
          </p>
        
      </div>

      <div id="repository_description_edit" style="display:none;" class="inline-edit">
        <form action="/ihh/dart/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="2e1b9efa608892dec046635b7eab90a702157c01" /></div>
          <input type="hidden" name="field" value="repository_description">
          <input type="text" class="textfield" name="value" value="DNA, Amino Acid and RNA Tests">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      
      <div class="repository-homepage" id="repository_homepage" rel="repository_homepage_edit">
        <p><a href="http://biowiki.org/DART" rel="nofollow">http://biowiki.org/DART</a></p>
      </div>

      <div id="repository_homepage_edit" style="display:none;" class="inline-edit">
        <form action="/ihh/dart/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="2e1b9efa608892dec046635b7eab90a702157c01" /></div>
          <input type="hidden" name="field" value="repository_homepage">
          <input type="text" class="textfield" name="value" value="http://biowiki.org/DART">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>
      </div>
      <div class="rule "></div>
      <div class="url-box">
  

  <ul class="clone-urls">
    
      
      <li class="http_clone_url"><a href="https://github.com/ihh/dart.git" data-permissions="Read-Only">HTTP</a></li>
      <li class="public_clone_url"><a href="git://github.com/ihh/dart.git" data-permissions="Read-Only">Git Read-Only</a></li>
    
    
  </ul>
  <input type="text" spellcheck="false" class="url-field" />
        <span style="display:none" id="clippy_3724" class="url-box-clippy"></span>
      <span id="clippy_tooltip_clippy_3724" class="clippy-tooltip tooltipped" title="copy to clipboard">
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="14"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_3724&amp;copied=&amp;copyto=">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"
             width="14"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_3724&amp;copied=&amp;copyto="
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      </span>

  <p class="url-description"><strong>Read+Write</strong> access</p>
</div>

    </div>

    <div class="frame frame-center tree-finder" style="display:none" data-tree-list-url="/ihh/dart/tree-list/e1ff4d6b483bb64c89170c8babb9b4f75ec2a12c" data-blob-url-prefix="/ihh/dart/blob/e1ff4d6b483bb64c89170c8babb9b4f75ec2a12c">
      <div class="breadcrumb">
        <b><a href="/ihh/dart">dart</a></b> /
        <input class="tree-finder-input" type="text" name="query" autocomplete="off" spellcheck="false">
      </div>

      
        <div class="octotip">
          <p>
            <a href="/ihh/dart/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever">Dismiss</a>
            <strong>Octotip:</strong> You've activated the <em>file finder</em> by pressing <span class="kbd">t</span>
            Start typing to filter the file list. Use <span class="kbd badmono">↑</span> and <span class="kbd badmono">↓</span> to navigate,
            <span class="kbd">enter</span> to view files.
          </p>
        </div>
      

      <table class="tree-browser" cellpadding="0" cellspacing="0">
        <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
        <tr class="js-no-results no-results" style="display: none">
          <th colspan="2">No matching files</th>
        </tr>
        <tbody class="js-results-list">
        </tbody>
      </table>
    </div>

    <div id="jump-to-line" style="display:none">
      <h2>Jump to Line</h2>
      <form>
        <input class="textfield" type="text">
        <div class="full-button">
          <button type="submit" class="classy">
            <span>Go</span>
          </button>
        </div>
      </form>
    </div>


        

      </div><!-- /.pagehead -->

      

  













  <div class="commit commit-tease js-details-container">
  
  <p class="commit-title">
    <a href="/ihh/dart/commit/e1ff4d6b483bb64c89170c8babb9b4f75ec2a12c">fixed gcc 4.6 compilation bugs</a>
    
  </p>
  
  <div class="commit-meta">
    <a href="/ihh/dart/commit/e1ff4d6b483bb64c89170c8babb9b4f75ec2a12c" class="sha-block">commit <span class="sha">e1ff4d6b48</span></a>

    <div class="authorship">
      
      <img src="https://secure.gravatar.com/avatar/7ed1d65041d341ceebb017f813acfe85?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="20" height="20" class="gravatar" />
      <span class="author-name">Ian Holmes (ihh)</span>
      authored <time class="js-relative-date" datetime="2011-09-07T14:59:55-07:00" title="2011-09-07 14:59:55">September 07, 2011</time>

      
    </div>
  </div>
</div>




  <div id="slider">

  

    <div class="breadcrumb" data-path="perl/stockholm2fasta.pl/">
      <b><a href="/ihh/dart/tree/efc8957db93eade77d12729515e4d8a26d9d0dd9" class="js-rewrite-sha">dart</a></b> / <a href="/ihh/dart/tree/efc8957db93eade77d12729515e4d8a26d9d0dd9/perl" class="js-rewrite-sha">perl</a> / stockholm2fasta.pl       <span style="display:none" id="clippy_693" class="clippy">perl/stockholm2fasta.pl</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_693&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_693&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div class="frames">
      <div class="frame frame-center" data-path="perl/stockholm2fasta.pl/" data-permalink-url="/ihh/dart/blob/efc8957db93eade77d12729515e4d8a26d9d0dd9/perl/stockholm2fasta.pl" data-title="perl/stockholm2fasta.pl at master from ihh/dart - GitHub" data-type="blob">
        
          <ul class="big-actions">
            
            <li><a class="file-edit-link minibutton" href="/ihh/dart/edit/__current_ref__/perl/stockholm2fasta.pl"><span>Edit this file</span></a></li>
          </ul>
        

        <div id="files">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><img alt="Txt" height="16" src="https://a248.e.akamai.net/assets.github.com/images/icons/txt.png" width="16" /></span>
                <span class="mode" title="File Mode">100755</span>
                
                  <span>64 lines (58 sloc)</span>
                
                <span>1.398 kb</span>
              </div>
              <ul class="actions">
                <li><a href="/ihh/dart/raw/master/perl/stockholm2fasta.pl" id="raw-url">raw</a></li>
                
                  <li><a href="/ihh/dart/blame/master/perl/stockholm2fasta.pl">blame</a></li>
                
                <li><a href="/ihh/dart/commits/master/perl/stockholm2fasta.pl">history</a></li>
              </ul>
            </div>
            
  <div class="data type-perl">
    
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
</pre>
          </td>
          <td width="100%">
            
              
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c1">#!/usr/bin/env perl -w</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="k">my</span> <span class="nv">$columns</span> <span class="o">=</span> <span class="mi">50</span><span class="p">;</span></div><div class='line' id='LC4'><span class="k">my</span> <span class="nv">$gapped</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="k">my</span> <span class="nv">$progname</span> <span class="o">=</span> <span class="nv">$0</span><span class="p">;</span></div><div class='line' id='LC7'><span class="nv">$progname</span> <span class="o">=~</span> <span class="sr">s/^.*?([^\/]+)$/$1/</span><span class="p">;</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="k">my</span> <span class="nv">$usage</span> <span class="o">=</span> <span class="s">&quot;Usage: $progname [&lt;Stockholm file(s)&gt;]\n&quot;</span><span class="p">;</span></div><div class='line' id='LC10'><span class="nv">$usage</span> <span class="o">.=</span>   <span class="s">&quot;             [-h] print this help message\n&quot;</span><span class="p">;</span></div><div class='line' id='LC11'><span class="nv">$usage</span> <span class="o">.=</span>   <span class="s">&quot;             [-g] write gapped FASTA output\n&quot;</span><span class="p">;</span></div><div class='line' id='LC12'><span class="nv">$usage</span> <span class="o">.=</span>   <span class="s">&quot;             [-s] sort sequences by name\n&quot;</span><span class="p">;</span></div><div class='line' id='LC13'><span class="nv">$usage</span> <span class="o">.=</span>   <span class="s">&quot;      [-c &lt;cols&gt;] number of columns for FASTA output (default is $columns)\n&quot;</span><span class="p">;</span></div><div class='line' id='LC14'><span class="c1"># parse cmd-line opts</span></div><div class='line' id='LC15'><span class="k">my</span> <span class="nv">@argv</span><span class="p">;</span></div><div class='line' id='LC16'><span class="k">while</span> <span class="p">(</span><span class="nv">@ARGV</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">my</span> <span class="nv">$arg</span> <span class="o">=</span> <span class="nb">shift</span><span class="p">;</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="nv">$arg</span> <span class="ow">eq</span> <span class="s">&quot;-h&quot;</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC19'>	<span class="nb">die</span> <span class="nv">$usage</span><span class="p">;</span></div><div class='line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span> <span class="k">elsif</span> <span class="p">(</span><span class="nv">$arg</span> <span class="ow">eq</span> <span class="s">&quot;-g&quot;</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC21'>	<span class="nv">$gapped</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span> <span class="k">elsif</span> <span class="p">(</span><span class="nv">$arg</span> <span class="ow">eq</span> <span class="s">&quot;-s&quot;</span><span class="p">){</span></div><div class='line' id='LC23'>	<span class="nv">$sorted</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span> <span class="k">elsif</span> <span class="p">(</span><span class="nv">$arg</span> <span class="ow">eq</span> <span class="s">&quot;-c&quot;</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC25'>	<span class="nb">defined</span> <span class="p">(</span><span class="nv">$columns</span> <span class="o">=</span> <span class="nb">shift</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">die</span> <span class="nv">$usage</span><span class="p">;</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span> <span class="k">else</span> <span class="p">{</span></div><div class='line' id='LC27'>	<span class="nb">push</span> <span class="nv">@argv</span><span class="p">,</span> <span class="nv">$arg</span><span class="p">;</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC29'><span class="p">}</span></div><div class='line' id='LC30'><span class="nv">@ARGV</span> <span class="o">=</span> <span class="nv">@argv</span><span class="p">;</span></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'><span class="k">my</span> <span class="nv">%seq</span><span class="p">;</span></div><div class='line' id='LC33'><span class="k">while</span> <span class="p">(</span><span class="o">&lt;&gt;</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">next</span> <span class="k">unless</span> <span class="sr">/\S/</span><span class="p">;</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">next</span> <span class="k">if</span> <span class="sr">/^\s*\#/</span><span class="p">;</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="sr">/^\s*\/\//</span><span class="p">)</span> <span class="p">{</span> <span class="n">printseq</span><span class="p">()</span> <span class="p">}</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span> <span class="p">{</span></div><div class='line' id='LC38'>	<span class="nb">chomp</span><span class="p">;</span></div><div class='line' id='LC39'>	<span class="k">my</span> <span class="p">(</span><span class="nv">$name</span><span class="p">,</span> <span class="nv">$seq</span><span class="p">)</span> <span class="o">=</span> <span class="nb">split</span><span class="p">;</span></div><div class='line' id='LC40'>	<span class="nv">$seq</span> <span class="o">=~</span> <span class="sr">s/[\.\-]//g</span> <span class="k">unless</span> <span class="nv">$gapped</span><span class="p">;</span></div><div class='line' id='LC41'>	<span class="nv">$seq</span><span class="p">{</span><span class="nv">$name</span><span class="p">}</span> <span class="o">.=</span> <span class="nv">$seq</span><span class="p">;</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC43'><span class="p">}</span></div><div class='line' id='LC44'><span class="n">printseq</span><span class="p">();</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'><span class="k">sub </span><span class="nf">printseq</span> <span class="p">{</span></div><div class='line' id='LC47'>	<span class="k">if</span><span class="p">(</span><span class="nv">$sorted</span><span class="p">){</span></div><div class='line' id='LC48'>		<span class="k">foreach</span> <span class="nv">$key</span> <span class="p">(</span><span class="nb">sort</span> <span class="nb">keys</span> <span class="nv">%seq</span><span class="p">){</span></div><div class='line' id='LC49'>			<span class="k">print</span> <span class="s">&quot;&gt;$key\n&quot;</span><span class="p">;</span></div><div class='line' id='LC50'>			<span class="k">for</span> <span class="p">(</span><span class="k">my</span> <span class="nv">$i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="nv">$i</span> <span class="o">&lt;</span> <span class="nb">length</span> <span class="nv">$seq</span><span class="p">{</span><span class="nv">$key</span><span class="p">};</span> <span class="nv">$i</span> <span class="o">+=</span> <span class="nv">$columns</span><span class="p">){</span></div><div class='line' id='LC51'>				<span class="k">print</span> <span class="nb">substr</span><span class="p">(</span><span class="nv">$seq</span><span class="p">{</span><span class="nv">$key</span><span class="p">},</span> <span class="nv">$i</span><span class="p">,</span> <span class="nv">$columns</span><span class="p">),</span> <span class="s">&quot;\n&quot;</span><span class="p">;</span></div><div class='line' id='LC52'>			<span class="p">}</span></div><div class='line' id='LC53'>		<span class="p">}</span></div><div class='line' id='LC54'>	<span class="p">}</span> <span class="k">else</span><span class="p">{</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;		<span class="k">while</span> <span class="p">(</span><span class="k">my</span> <span class="p">(</span><span class="nv">$name</span><span class="p">,</span> <span class="nv">$seq</span><span class="p">)</span> <span class="o">=</span> <span class="nb">each</span> <span class="nv">%seq</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC56'>			<span class="k">print</span> <span class="s">&quot;&gt;$name\n&quot;</span><span class="p">;</span></div><div class='line' id='LC57'>			<span class="k">for</span> <span class="p">(</span><span class="k">my</span> <span class="nv">$i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="nv">$i</span> <span class="o">&lt;</span> <span class="nb">length</span> <span class="nv">$seq</span><span class="p">;</span> <span class="nv">$i</span> <span class="o">+=</span> <span class="nv">$columns</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC58'>	    			<span class="k">print</span> <span class="nb">substr</span> <span class="p">(</span><span class="nv">$seq</span><span class="p">,</span> <span class="nv">$i</span><span class="p">,</span> <span class="nv">$columns</span><span class="p">),</span> <span class="s">&quot;\n&quot;</span><span class="p">;</span></div><div class='line' id='LC59'>			<span class="p">}</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;	 	<span class="p">}</span></div><div class='line' id='LC61'>	<span class="p">}</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nv">%seq</span> <span class="o">=</span> <span class="p">();</span></div><div class='line' id='LC63'><span class="p">}</span></div><div class='line' id='LC64'><br/></div></pre></div>
              
            
          </td>
        </tr>
      </table>
    
  </div>


          </div>
        </div>
      </div>
    </div>
  

  </div>


<div class="frame frame-loading" style="display:none;" data-tree-list-url="/ihh/dart/tree-list/e1ff4d6b483bb64c89170c8babb9b4f75ec2a12c" data-blob-url-prefix="/ihh/dart/blob/e1ff4d6b483bb64c89170c8babb9b4f75ec2a12c">
  <img src="https://a248.e.akamai.net/assets.github.com/images/modules/ajax/big_spinner_336699.gif" height="32" width="32">
</div>

    </div>
  
      
    </div>

    <!--**************
     FOOTER
     **************-->
    <div id="footer" >
      <div class="upper_footer">
        <div class="site" class="clearfix">

        <!--[if IE]><h4 id="blacktocat_ie">GitHub Links</h4><![endif]-->
        <![if !IE]><h4 id="blacktocat">GitHub Links</h4><![endif]>

        <ul class="footer_nav">
          <h4>GitHub</h4>
          <li><a href="https://github.com/about">About</a></li>
          <li><a href="https://github.com/blog">Blog</a></li>
          <li><a href="https://github.com/features">Features</a></li>
          <li><a href="https://github.com/contact">Contact &amp; Support</a></li>
          <li><a href="https://github.com/training">Training</a></li>
          <li><a href="http://status.github.com/">Site Status</a></li>
        </ul>

        <ul class="footer_nav">
          <h4>Tools</h4>
          <li><a href="http://mac.github.com/">GitHub for Mac</a></li>
          <li><a href="http://mobile.github.com/">Issues for iPhone</a></li>
          <li><a href="https://gist.github.com">Gist: Code Snippets</a></li>
          <li><a href="http://fi.github.com/">Enterprise Install</a></li>
          <li><a href="http://jobs.github.com/">Job Board</a></li>
        </ul>

        <ul class="footer_nav">
          <h4>Extras</h4>
          <li><a href="http://shop.github.com/">GitHub Shop</a></li>
          <li><a href="http://octodex.github.com/">The Octodex</a></li>
        </ul>

        <ul class="footer_nav">
          <h4>Documentation</h4>
          <li><a href="http://help.github.com/">GitHub Help</a></li>
          <li><a href="http://developer.github.com/">Developer API</a></li>
          <li><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
          <li><a href="http://pages.github.com/">GitHub Pages</a></li>
        </ul>

        </div><!-- /.site -->
      </div><!-- /.upper_footer -->

      <div class="lower_footer">
        <div class="site" class="clearfix">

        <!--[if IE]><div id="legal_ie"><![endif]-->
        <![if !IE]><div id="legal"><![endif]>
              
              <ul>
                <li><a href="https://github.com/site/terms">Terms of Service</a></li>
                <li><a href="https://github.com/site/privacy">Privacy</a></li>
                <li><a href="https://github.com/security">Security</a></li>
              </ul>
              

              <p>&copy; 2011 <span id="_rrt" title="0.04863s from fe7.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
            </div><!-- /#legal or /#legal_ie-->

          
          <div class="sponsor">
              <a href="http://www.rackspace.com" class="logo">
                <img alt="Dedicated Server" height="36" src="https://a248.e.akamai.net/assets.github.com/images/modules/footer/rackspace_logo.png?v2" width="38" />
              </a>
              Powered by the <a href="http://www.rackspace.com ">Dedicated
              Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
              Computing</a> of Rackspace Hosting<span>&reg;</span>
          </div>
          
        </div><!-- /.site -->
      </div><!-- /.lower_footer -->
    </div><!-- /#footer -->

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selected down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selected up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle select target</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column middle">
        <dl class="keyboard-mappings">
          <dt>I</dt>
          <dd>Mark selected as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>U</dt>
          <dd>Mark selected as unread</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>e</dt>
          <dd>Close selected</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Remove selected from view</dd>
        </dl>
      </div><!-- /.column.middle -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>
</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:
> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>
    

    
    
    
    <script type="text/javascript">(function(){var d=document;var e=d.createElement("script");e.async=true;e.src="https://d1ros97qkrwjf5.cloudfront.net/16/eum/rum.js";e.type="text/javascript";var s=d.getElementsByTagName("script")[0];s.parentNode.insertBefore(e,s);})();NREUMQ.push(["nrf2","beacon-1.newrelic.com","2f94e4d8c2",64799,"dw1bEBZcX1RWRhoEClsAGhcMXEQ=",0,45,new Date().getTime()])</script>
  </body>
</html>

