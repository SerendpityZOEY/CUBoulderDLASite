<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML+RDFa 1.0//EN"
  "http://www.w3.org/MarkUp/DTD/xhtml-rdfa-1.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" version="XHTML+RDFa 1.0" dir="ltr"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:dc="http://purl.org/dc/terms/"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:og="http://ogp.me/ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:sioc="http://rdfs.org/sioc/ns#"
  xmlns:sioct="http://rdfs.org/sioc/types#"
  xmlns:skos="http://www.w3.org/2004/02/skos/core#"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema#">

<head profile="http://www.w3.org/1999/xhtml/vocab">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,t,n){function r(n){if(!t[n]){var o=t[n]={exports:{}};e[n][0].call(o.exports,function(t){var o=e[n][1][t];return r(o||t)},o,o.exports)}return t[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(e,t,n){function r(){}function o(e,t,n){return function(){return i(e,[(new Date).getTime()].concat(u(arguments)),t?null:this,n),t?void 0:this}}var i=e("handle"),a=e(2),u=e(3),c=e("ee").get("tracer"),f=NREUM;"undefined"==typeof window.newrelic&&(newrelic=f);var s=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit"],l="api-",p=l+"ixn-";a(s,function(e,t){f[t]=o(l+t,!0,"api")}),f.addPageAction=o(l+"addPageAction",!0),f.setCurrentRouteName=o(l+"routeName",!0),t.exports=newrelic,f.interaction=function(){return(new r).get()};var d=r.prototype={createTracer:function(e,t){var n={},r=this,o="function"==typeof t;return i(p+"tracer",[Date.now(),e,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[Date.now(),r,o],n),o)try{return t.apply(this,arguments)}finally{c.emit("fn-end",[Date.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,t){d[t]=o(p+t)}),newrelic.noticeError=function(e){"string"==typeof e&&(e=new Error(e)),i("err",[e,(new Date).getTime()])}},{}],2:[function(e,t,n){function r(e,t){var n=[],r="",i=0;for(r in e)o.call(e,r)&&(n[i]=t(r,e[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;t.exports=r},{}],3:[function(e,t,n){function r(e,t,n){t||(t=0),"undefined"==typeof n&&(n=e?e.length:0);for(var r=-1,o=n-t||0,i=Array(o<0?0:o);++r<o;)i[r]=e[t+r];return i}t.exports=r},{}],ee:[function(e,t,n){function r(){}function o(e){function t(e){return e&&e instanceof r?e:e?c(e,u,i):i()}function n(n,r,o){if(!p.aborted){e&&e(n,r,o);for(var i=t(o),a=v(n),u=a.length,c=0;c<u;c++)a[c].apply(i,r);var f=s[w[n]];return f&&f.push([y,n,r,i]),i}}function d(e,t){b[e]=v(e).concat(t)}function v(e){return b[e]||[]}function g(e){return l[e]=l[e]||o(n)}function m(e,t){f(e,function(e,n){t=t||"feature",w[n]=t,t in s||(s[t]=[])})}var b={},w={},y={on:d,emit:n,get:g,listeners:v,context:t,buffer:m,abort:a,aborted:!1};return y}function i(){return new r}function a(){(s.api||s.feature)&&(p.aborted=!0,s=p.backlog={})}var u="nr@context",c=e("gos"),f=e(2),s={},l={},p=t.exports=o();p.backlog=s},{}],gos:[function(e,t,n){function r(e,t,n){if(o.call(e,t))return e[t];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[t]=r,r}var o=Object.prototype.hasOwnProperty;t.exports=r},{}],handle:[function(e,t,n){function r(e,t,n,r){o.buffer([e],r),o.emit(e,t,n)}var o=e("ee").get("handle");t.exports=r,r.ee=o},{}],id:[function(e,t,n){function r(e){var t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");t.exports=r},{}],loader:[function(e,t,n){function r(){if(!h++){var e=y.info=NREUM.info,t=l.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&t))return f.abort();c(b,function(t,n){e[t]||(e[t]=n)}),u("mark",["onload",a()],null,"api");var n=l.createElement("script");n.src="https://"+e.agent,t.parentNode.insertBefore(n,t)}}function o(){"complete"===l.readyState&&i()}function i(){u("mark",["domContent",a()],null,"api")}function a(){return(new Date).getTime()}var u=e("handle"),c=e(2),f=e("ee"),s=window,l=s.document,p="addEventListener",d="attachEvent",v=s.XMLHttpRequest,g=v&&v.prototype;NREUM.o={ST:setTimeout,CT:clearTimeout,XHR:v,REQ:s.Request,EV:s.Event,PR:s.Promise,MO:s.MutationObserver},e(1);var m=""+location,b={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-998.min.js"},w=v&&g&&g[p]&&!/CriOS/.test(navigator.userAgent),y=t.exports={offset:a(),origin:m,features:{},xhrWrappable:w};l[p]?(l[p]("DOMContentLoaded",i,!1),s[p]("load",r,!1)):(l[d]("onreadystatechange",o),s[d]("onload",r)),u("mark",["firstbyte",a()],null,"api");var h=0},{}]},{},["loader"]);</script>
<link rel="shortcut icon" href="http://www.colorado.edu/engineering/sites/default/files/cu_favicon.png" type="image/png" />
<meta name="Generator" content="Drupal 7 (http://drupal.org)" />
  <title>Page not found | College of Engineering and Applied Science | University of Colorado Boulder</title>
  <link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_Fu8ZLCLZJ5gA1Zo82CrwHP0xpsZtzX3Z59S4-pc6hxk.css" media="screen" />
<link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_kbp4t0tna8Hls9HB6EuXY5pM_mxI6rw0RcTK-aQZu38.css" media="all" />
<link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_F4YL9JrSGrJ-s1cqPl6zyQO7iZSpc2K9CBWEkff8DYw.css" media="all" />
<link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_ZQsffyFr2Wn8HlwCntd6vROiPj3CC-clLc0IayqhtNU.css" media="all" />
<link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_rdm2jD2My91iJsByPitd8xZ3CQ2jY7HBF9BbItpngko.css" media="all" />
<link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU.css" media="all" />
<link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_h7rXjqzd0SKUqfJXRX0i-R7tYhSE8eb4dlkjF0zPgGM.css" media="print" />
<link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_GNnBGDQtfKgeOlkW_danoVLfWZ-zCR0snCQUVq-iQiA.css" media="screen" />
<link type="text/css" rel="stylesheet" href="http://www.colorado.edu/engineering/sites/default/files/css/css_47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU.css" media="all" />
  <script type="text/javascript" src="http://www.colorado.edu/engineering/sites/default/files/js/js_UWQINlriydSoeSiGQxToOUdv493zEa7dpsXC1OtYlZU.js"></script>
<script type="text/javascript" src="http://www.colorado.edu/engineering/sites/default/files/js/js_4k3gEinq8vqEMRszlC2h1-sJcJYAs1PhgpRoYE-PqMI.js"></script>
<script type="text/javascript" src="http://www.colorado.edu/engineering/sites/default/files/js/js_tU91BUWAG2hFAKpsgp4IxDknAfpFxFANsLXyW_KXXv8.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
jQuery(document).ready(function () { jQuery("div.js-accordion").accordion({ autoHeight: false, active:false, collapsible: true }); });
//--><!]]>
</script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
jQuery(document).ready(function () { jQuery("div.js-tabs").tabs(); });
//--><!]]>
</script>
<script type="text/javascript" src="http://www.colorado.edu/engineering/sites/default/files/js/js_75GUMsOqWgyVaVof0wqUbsHLxeEZJeDU_YhLg6Xc8_0.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
window.CKEDITOR_BASEPATH = '/engineering/sites/all/libraries/ckeditor/'
//--><!]]>
</script>
<script type="text/javascript" src="http://www.colorado.edu/engineering/sites/default/files/js/js_IDBX5SzkJ9gGNq7x-qOE_2DZsexqguTJQGMKvi4w-Uw.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
var _gaq = _gaq || [];_gaq.push(["_setAccount", "UA-25752450-1"]);_gaq.push(["_trackPageview", "/404.html?page=" + document.location.pathname + document.location.search + "&from=" + document.referrer]);(function() {var ga = document.createElement("script");ga.type = "text/javascript";ga.async = true;ga.src = "http://www.colorado.edu/engineering/sites/default/files/googleanalytics/ga.js?ofoa2f";var s = document.getElementsByTagName("script")[0];s.parentNode.insertBefore(ga, s);})();
//--><!]]>
</script>
<script type="text/javascript" src="http://www.colorado.edu/engineering/sites/default/files/js/js_a_XWH2S1EQaU85ypMDyQGiUfzPFez1IOZKxHnhGkv3E.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
jQuery.extend(Drupal.settings, {"basePath":"\/engineering\/","pathPrefix":"","ajaxPageState":{"theme":"reach","theme_token":"AEU4EFIZfXvfH99IGaFnc6lesXQJByKlYM6D2qBAsWA","js":{"sites\/all\/modules\/contrib\/backstretch\/bs.js":1,"sites\/all\/modules\/features\/cu_search\/cu_search.js":1,"misc\/jquery.js":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"misc\/ui\/jquery.ui.core.min.js":1,"misc\/ui\/jquery.ui.widget.min.js":1,"misc\/ui\/jquery.ui.accordion.min.js":1,"misc\/ui\/jquery.ui.tabs.min.js":1,"misc\/form.js":1,"sites\/all\/libraries\/colorbox\/colorbox\/jquery.colorbox-min.js":1,"sites\/all\/modules\/contrib\/colorbox\/js\/colorbox.js":1,"sites\/all\/modules\/contrib\/colorbox\/styles\/default\/colorbox_default_style.js":1,"sites\/all\/modules\/contrib\/colorbox\/js\/colorbox_load.js":1,"sites\/all\/modules\/contrib\/context_accordion\/context_accordion.js":1,"0":1,"1":1,"sites\/all\/modules\/contrib\/image_caption\/image_caption.min.js":1,"sites\/all\/modules\/contrib\/views_slideshow\/js\/views_slideshow.js":1,"sites\/all\/modules\/contrib\/extlink\/extlink.js":1,"sites\/all\/libraries\/backstretch\/jquery.backstretch.js":1,"sites\/all\/libraries\/waypoints\/waypoints.min.js":1,"sites\/all\/libraries\/scrollto\/jquery.scrollTo-min.js":1,"2":1,"sites\/all\/modules\/contrib\/google_analytics\/googleanalytics.js":1,"3":1,"misc\/collapse.js":1},"css":{"sites\/all\/themes\/cu_bootstrap\/styles\/framework\/reset.css":1,"sites\/all\/themes\/cu_bootstrap\/styles\/framework\/text.css":1,"sites\/all\/themes\/cu_bootstrap\/styles\/framework\/960.css":1,"sites\/all\/themes\/cu_bootstrap\/styles\/framework\/debug.css":1,"sites\/all\/themes\/reach\/styles\/framework\/reset.css":1,"sites\/all\/themes\/reach\/styles\/framework\/text.css":1,"sites\/all\/themes\/reach\/styles\/framework\/960.css":1,"sites\/all\/themes\/reach\/styles\/framework\/debug.css":1,"modules\/system\/system.base.css":1,"modules\/system\/system.menus.css":1,"modules\/system\/system.messages.css":1,"modules\/system\/system.theme.css":1,"misc\/ui\/jquery.ui.core.css":1,"misc\/ui\/jquery.ui.theme.css":1,"misc\/ui\/jquery.ui.accordion.css":1,"misc\/ui\/jquery.ui.tabs.css":1,"sites\/all\/modules\/contrib\/date\/date_api\/date.css":1,"modules\/field\/theme\/field.css":1,"sites\/all\/modules\/contrib\/google_appliance\/theme\/google_appliance.css":1,"modules\/node\/node.css":1,"modules\/user\/user.css":1,"sites\/all\/modules\/contrib\/views\/css\/views.css":1,"sites\/all\/modules\/contrib\/colorbox\/styles\/default\/colorbox_default_style.css":1,"sites\/all\/modules\/contrib\/context_accordion\/context_accordion.css":1,"sites\/all\/modules\/contrib\/ctools\/css\/ctools.css":1,"sites\/all\/modules\/contrib\/views_slideshow\/views_slideshow.css":1,"sites\/all\/modules\/contrib\/extlink\/extlink.css":1,"sites\/all\/modules\/contrib\/backstretch\/backstretch.css":1,"sites\/all\/modules\/features\/cu_search\/cu_search.css":1,"sites\/all\/themes\/cu_bootstrap\/styles\/styles.css":1,"sites\/all\/themes\/cu_bootstrap\/styles\/common.css":1,"sites\/all\/themes\/cu_bootstrap\/styles\/slider.css":1,"sites\/all\/themes\/cu_bootstrap\/styles\/images.css":1,"sites\/all\/themes\/cu_bootstrap\/styles\/quicktabs-styles.css":1,"sites\/all\/themes\/cu_bootstrap\/jquery-ui\/css\/custom-theme\/jquery-ui-1.8.17.custom.css":1,"sites\/all\/themes\/reach\/styles\/context_accordion.css":1,"sites\/all\/themes\/reach\/styles\/print.css":1,"sites\/all\/themes\/reach\/styles\/styles.css":1,"sites\/all\/themes\/reach\/styles\/my_blocks.css":1,"sites\/all\/themes\/reach\/styles\/fonts.css":1,"sites\/all\/themes\/reach\/styles\/common.css":1,"sites\/all\/themes\/reach\/styles\/slider.css":1,"sites\/all\/themes\/reach\/styles\/images.css":1,"sites\/all\/themes\/reach\/styles\/quicktabs-styles.css":1,"sites\/all\/themes\/reach\/jquery-ui\/css\/custom-theme\/jquery-ui-1.8.17.custom.css":1,"sites\/all\/themes\/reach\/styles\/jquery.ul.accordion.css":1,"sites\/all\/themes\/reach\/styles\/jcarousel-default.css":1,"sites\/all\/themes\/reach\/fonts\/3.css":1}},"colorbox":{"opacity":"0.85","current":"{current} of {total}","previous":"\u00ab Prev","next":"Next \u00bb","close":"Close","maxWidth":"100%","maxHeight":"100%","fixed":true,"__drupal_alter_by_ref":["default"]},"jcarousel":{"ajaxPath":"\/engineering\/jcarousel\/ajax\/views"},"extlink":{"extTarget":"_blank","extClass":0,"extSubdomains":0,"extExclude":"colorado.edu\/engineering","extInclude":"colorado.edu","extAlert":0,"extAlertText":"This link will take you to an external web site. We are not responsible for their content.","mailtoClass":0},"backstretchURL":"\/engineering\/sites\/default\/files\/backstretch-dlc2.jpg","backstretchMinWidth":"1100","backstretchScroller":true,"backstretchScrollerAdj":"-125px","backstretchScrollTo":true,"googleanalytics":{"trackOutbound":1,"trackMailto":1,"trackDownload":1,"trackDownloadExtensions":"7z|aac|arc|arj|asf|asx|avi|bin|csv|doc|exe|flv|gif|gz|gzip|hqx|jar|jpe?g|js|mp(2|3|4|e?g)|mov(ie)?|msi|msp|pdf|phps|png|ppt|qtm?|ra(m|r)?|sea|sit|tar|tgz|torrent|txt|wav|wma|wmv|wpd|xls|xml|z|zip"},"urlIsAjaxTrusted":{"\/engineering\/WebResource.axd?d=yWuHttwMAr-wfNjU7zoge2la36zCNQdXlUq6jm1UEr1_HH7xDEy-DLzTnGxXTidUbszcIqrg6NnPE5ylOFsR_0Z9Lns1\u0026t=635588366547524888":true}});
//--><!]]>
</script>
</head>
<body class="html not-front not-logged-in no-sidebars page-node page-node- page-node-12" >
  <div id="skip-link">
    <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
  </div>
    <div id="page-wrapper">
  <div id="page" class="clearfix">
    <div id="header-wrapper">
      <div id="site-header" class="clearfix container-12">
        <div id="branding" class="grid-8 alpha">
            	        <div id="logo"><a href="/engineering/">College of Engineering and Applied Science | University of Colorado Boulder</a></div>
  	              </div><!-- /#branding -->
        
        <div id="search" class="grid-4 omega">
                        <div class="region region-search">
    <div id="block-google-appliance-ga-block-search-form" class="block block-google-appliance">

    
  <div class="content">
    <form action="/engineering/WebResource.axd?d=yWuHttwMAr-wfNjU7zoge2la36zCNQdXlUq6jm1UEr1_HH7xDEy-DLzTnGxXTidUbszcIqrg6NnPE5ylOFsR_0Z9Lns1&amp;t=635588366547524888" method="post" id="google-appliance-block-form" accept-charset="UTF-8"><div><div class="container-inline">
      <h2 class="element-invisible">Search Google Appliance</h2>
    <div class="cu-search clearfix"><div class="form-item form-type-textfield form-item-search-keys">
  <label class="element-invisible" for="edit-search-keys">Enter the terms you wish to search for. </label>
 <input type="text" id="edit-search-keys" name="search_keys" value="" size="15" maxlength="128" class="form-text" />
</div>
<div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit" name="op" value="Search" class="form-submit" /></div></div><div class="culinks"><strong>CU:</strong> <a href="/">Home</a> &bull; <a href="/atoz">A to Z</a> &bull; <a href="/campusmap">Campus Map</a></div><input type="hidden" name="form_build_id" value="form-EBQHLmWkMXFEcV2OzYZpjQu3QSVQw7UwZd-jo-eQVyc" />
<input type="hidden" name="form_id" value="google_appliance_block_form" />
  
</div>
</div></form>  </div>
</div>
  </div>
                  </div><!-- /#search -->

        <img src="/engineering/sites/all/themes/reach/images/print-logo.png" id="print-logo" />

      </div><!-- /#site-header -->
    </div>
     <img src="/engineering/sites/all/themes/reach/images/print-logo.png" id="print-logo" />
        
    <div id="alerts">
          </div>
    
          <div id="no-main-menu"></div>  
      
    
  
      
      
  
    <div id="main-wrapper" class="column-1">
       
    
    
    
      
      
         <div id="main-top-curves"></div>
      <div id="main" class="clearfix container-12">
                                
        
      
                
            
  	    <div id="content" class="clearfix  grid-12 ">
          <div id="main-content" class="region clearfix">
         
            
                        
                            <h1 class="title" id="page-title">Page not found</h1>
                                         
                        <div class="region region-content">
    <div id="block-system-main" class="block block-system">

    
  <div class="content">
    The requested page "/engineering/WebResource.axd?d=yWuHttwMAr-wfNjU7zoge2la36zCNQdXlUq6jm1UEr1_HH7xDEy-DLzTnGxXTidUbszcIqrg6NnPE5ylOFsR_0Z9Lns1&amp;t=635588366547524888" could not be found.  </div>
</div>
  </div>
                   </div><!-- /#main-content -->
  	    </div><!-- /#content -->
  	
  	    
    
	
          <div id="sidebar-second" class="grid-3 sidebar">   
			          </div>

  
	  	
  	  </div><!-- /#main -->

      <div class="clear"></div>
    </div><!-- /#main_wrapper -->
          <div id="after-content-wrapper">
  	    <div id="after-content" class="clearfix">
  	        <div class="region region-after-content">
    <div id="block-block-567" class="block block-block grid-4 new-block-row">

    
  <div class="content">
    <script type="text/javascript">
<!--//--><![CDATA[// ><!--


(function() {
var sz = document.createElement('script'); sz.type = 'text/javascript'; sz.async = true;
sz.src = '//us1.siteimprove.com/js/siteanalyze_80274.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sz, s);
})();


//--><!]]>
</script>  </div>
</div>
  </div>
	
  	    </div>
  	  </div>
        
	  	    <div id="other-bar" class="container-12 clearfix">
  	        <div class="region region-other-bar">
    <div id="block-block-29" class="block block-block">

    <h2>Connect with Us</h2>
  
  <div class="content">
    <p><a href="http://www.facebook.com/cuengineering"><img alt="Facebook" src="/engineering/sites/all/modules/custom/cu_social_connect/icons/round/facebook_32.png" style="width: 32px; height: 32px;" /></a><a href="https://twitter.com/cuengineering"><img alt="Twitter" src="/engineering/sites/all/modules/custom/cu_social_connect/icons/round/twitter_32.png" style="width: 32px; height: 32px;" /></a><a href="http://www.youtube.com/cuengr"><img alt="YouTube" src="/engineering/sites/all/modules/custom/cu_social_connect/icons/round/youtube_32.png" style="width: 32px; height: 32px;" /></a><a href="http://www.linkedin.com/groups/CU-Engineering-Alumni-University-Colorado-1815525"><img alt="LinkedIn" src="/engineering/sites/default/files/linkedin_32.png" style="width: 32px; height: 32px;" /></a></p>
<p><a href="/engineering/node/296">See All Social Media</a><br /><a href="/engineering/node/97">Faculty/Staff Directory</a><a href="http://events.colorado.edu/default.aspx?category=27-0,27-180,27-179"><br />
	Events Calendar</a><a href="/engineering/node/937"><br />
	News Releases</a><br /><a href="/engineering/node/839">Contact Us</a></p>
  </div>
</div>
<div id="block-block-2" class="block block-block">

    <h2><a href="/engineering/about/facilities-maps-and-directions" class="block-title-link">Maps and Directions</a></h2>
  
  <div class="content">
    <p><a href="/engineering/node/84"><img alt="" src="/engineering/sites/default/files/map.gif" style="width: 200px; height: 100px;" /></a></p>
  </div>
</div>
<div id="block-block-3" class="block block-block">

    <h2>Important Announcements</h2>
  
  <div class="content">
    <p><strong><em>CUEngineering: </em></strong> A publication for alumni and friends. Read the 2016 edition of CUEngineering magazine <a href="http://www.colorado.edu/cuengineering/" target="_blank">here</a>.</p>
  </div>
</div>
  </div>
	
  	  </div>
    
        
    
     <div id="site-info-wrapper">
		              
						  <div id="cu-info">
				            <a href="http://www.colorado.edu"><strong>University of Colorado Boulder</strong></a><br />
				            &copy; Regents of the University of Colorado<br />
				           <a href="http://www.colorado.edu/about/privacy-statement">Privacy</a> &bull; <a href="http://www.colorado.edu/about/legal-trademarks">Legal &amp; Trademarks</a>
				          </div>
			<div id="cu-info-right">
					<strong>	College of Engineering & Applied Science</strong><br/>
		<a href= "/engineering/node/103">Employment</a>	<br/>
		<a href= "/engineering/node/839">Contact Us</a>	
		</div>
		</div>
    <div class="container-12 clearfix">
      <div class="grid-4">
      </div>
    </div>


</div> <!-- /#page -->

</div><div id="foundation"></div> <!-- /#page-wrapper -->
	
  <ul class="footer-links links"><li class="0 first"><a href="/engineering/photos" class="more-photos">See More Photos</a></li>
<li class="1 last"><a href="/engineering/#backstretchmargin" id="backstretch-scrollto">View Photo</a></li>
</ul><script type="text/javascript" src="http://www.colorado.edu/engineering/sites/default/files/js/js_6m30tBwHYxp4ZtICt83MBE7yJdeNj9Oj3sEqHYuqhtc.js"></script>
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"77bdf6c909","applicationID":"34124724,34006488,34006198","transactionName":"ZARbNksCWkRYUE1eW11ObBBQTFFZXlpXUlFBCFcFFgpaU1xLF0dcQw==","queueTime":0,"applicationTime":215,"atts":"SENYQAMYSUo=","errorBeacon":"bam.nr-data.net","agent":""}</script></body>
</html>
