# -*-coding:utf-8-*-
import re

'''
test sub
'''

str1 = 'abcdefAbcaBC'
p = r'abc'
pattern = re.compile(p, re.I)

info = pattern.sub('222', str1, 2)
print info

info1 = pattern.subn('222', str1, 2)
print info1[0], info1[1]

import re

str1 = '''abcdefA aC'''
p = r'a\Sc'
pattern = re.compile(p, re.I)

info1 = pattern.subn('222', str1, 2)
print info1[0], info1[1]
print info1

info2 = re.escape(info1[0])
print info2

re.purge()

str2 = "12a32bc43jf3"
p = r"\d+"
it = re.finditer(p, str2)
for row in it:
    print row.group(0)


p = r'<td class="song_name">\s*<a title="[\s\S]+?" class="slide_down" href="javascript:;"></a>\s*<a title="([\s\S]+?)" href="([\s\S]+?)" target="_blank"><b class="key_red">[\s\S]+?</b></a>\s*</td>'
myStr = '''
<!doctype html>
<!--[if lt IE 7 ]> <html class="ie ie6"> <![endif]-->
<!--[if IE 7 ]>    <html class="ie ie7"> <![endif]-->
<!--[if IE 8 ]>    <html class="ie8"> <![endif]-->
<!--[if IE 9 ]>    <html class="ie9"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--><html lang="zh-CN"><!--<![endif]-->
<head>
	<meta charset="UTF-8" />
	<meta name="renderer" content="webkit" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge" />
	<meta name="data-spm" content="a1z1s" />
	<title>铏剧背闊充箰鎼滅储寮曟搸</title>
	<meta name="verify-v1" content="gNntuhTm2rH7Qa/GPp6lf0mIp9KQsjejNs+i1LZhG7U=" />
	<meta name="keywords" content="铏剧背闊充箰鎼滅储寮曟搸" />
	<meta name="description" content="铏剧背闊充箰鎼滅储寮曟搸" />

	<meta name="apple-itunes-app" content="app-id=595594905">
	<meta name="applicable-device" content="pc">
	<link href="http://res.xiami.net/static/common/base.css?ver=20151223-191455" media="all" rel="stylesheet" />

		<link href="http://res.xiami.net/??res/v3/css/global.css,res/v3/css/login.css,static/css/basic/core_mod.css,static/relation/css/name_card.css?ver=20151223-191455" media="all" rel="stylesheet" />

		<link href="http://res.xiami.net/??static/lib/jquery.jscrollpane.css,static/common/header.css,static/common/footer.css?ver=20151223-191455" media="all" rel="stylesheet" />

	<link href="http://res.xiami.net/??res/css/default/main15.css,res/css/default/mode15.css?ver=20151223-191455" media="all" rel="stylesheet" />
<link href="http://res.xiami.net/??res/css/default/group15.css,res/css/default/beta15.css?ver=20151223-191455" media="all" rel="stylesheet" />
<link href="http://res.xiami.net/??static/music/common/album.css,static/music/common/artist.css?ver=20151223-191455" media="all" rel="stylesheet" />

	<link href="http://res.xiami.net/static/common/old.css?ver=20151223-191455" media="all" rel="stylesheet" />

	<link href="http://img.xiami.net/favicon.ico" type="image/x-icon" rel="shortcut icon" />
	<link href="http://img.xiami.net/res/img/common/ipad/xiami_logo_apple.png" rel="apple-touch-icon" />
	<link href="http://www.xiami.com/opensearch.xml" type="application/opensearchdescription+xml" rel="search" title="Xiami Search"/>
	<link rel="alternate" type="application/atom+xml" title="铏剧背闊充箰姣忔棩绮鹃??" href="http://www.xiami.com/collect/feed">



	<style type="text/css">

		#header{   text-align: left;  zoom:1;  z-index:10; }
		#header .wrapper,#secondary .wrapper,#footer .wrapper{
			_width: expression(documentElement.clientWidth < 980? "980px" : documentElement.clientWidth > 1100? "1100px" : "auto");
		}

		.ie6 #secondary a.current{ background: none;}
		#header .primary .search .submit{ padding:0; cursor: pointer;}
		#header a,#secondary a{ text-decoration:none;}
		#header .user{vertical-align:top;}
		#header .auto_complete strong{ font-weight:normal;}
		#header .primary .user_popup .content ul .logout{ padding:0;}
		#header .content,#secondary .content{ overflow: visible;}
		#secondary{  text-align: left;}
		.no-shadow{ box-shadow: none !important; -moz-box-shadow: none !important; -webkit-box-shadow: none !important;}
		#footer{zoom: 1;}
	</style>



	<!--[if lte IE 8]>
	<link href="http://res.xiami.net/res/v3/css/login_iefix.css?v=20130521145542" rel="stylesheet" media="all" />
	<![endif]-->

	<!-- kirov start -->
	<script src="//g.alicdn.com/secdev/pointman/js/index.js" app="xiami"></script>
	<!-- kirov end -->

		<script type="text/javascript" src="http://res.xiami.net/??static/lib/jQuery/1.4.4/jquery.min.js,res/js/jquery/jqDnR.js,static/lib/jqModal.js,res/js/jquery/jquery.form.js,res/js/jquery/jquery.cookie.js,res/js/jquery/jquery.tools.js,res/v3/js/functions/index.js,res/js/default/xiami.js?ver=20151223-191455"></script>

		<script type="text/javascript" src="http://res.xiami.net/??static/js/lib/jquery.tmpl.min.js,static/js/app/relation.js,static/js/app/nameCard.js?ver=20151223-191455"></script>


	<script type="text/javascript" src="http://res.xiami.net/??static/lib/jquery.mousewheel.js,static/lib/jquery.jscrollpane.min.js,static/common/header_old.js,static/common/base.js?ver=20151223-191455"></script>


	<script>
	var _xiamitoken = $.cookie(\'_xiamitoken\'),
		_xiamiimg = \'http://img.xiami.net\',
		_xiamiuser = $.cookie(\'user\') || \'\',
		_athenaapiurl = \'ihi.xiami.com\';
	</script>

	<script type="text/javascript" src="http://res.xiami.net/static/music/common/frame.js?ver=20151223-191455"></script>


	<!-- google ads -->


<script type=\'text/javascript\'>
var googletag = googletag || {};
googletag.cmd = googletag.cmd || [];
googletag.cmd.push(function() {

googletag.defineSlot(\'/2315836/Muisc-Album_Right_300x250\', [300, 250], \'div-gpt-ad-1414398126484-0\').addService(googletag.pubads());
googletag.defineSlot(\'/2315836/Muisc-Album_Bottom_300x250\', [640, 100], \'div-gpt-ad-1414398685761-0\').addService(googletag.pubads());

googletag.defineSlot(\'/2315836/Music-Artist_Right_300x250\', [300, 250], \'div-gpt-ad-1414398815789-0\').addService(googletag.pubads());
googletag.defineSlot(\'/2315836/Music-Artist_Bottom_300x250\', [640, 100], \'div-gpt-ad-1414398865084-0\').addService(googletag.pubads());

googletag.defineSlot(\'/2315836/Collect-Homepage_Right_300x250\', [300, 250], \'div-gpt-ad-1414398966988-0\').addService(googletag.pubads());
googletag.defineSlot(\'/2315836/Collect-Homepage_Right2_300x250\', [300, 250], \'div-gpt-ad-1414399009160-0\').addService(googletag.pubads());

googletag.defineSlot(\'/2315836/閰嶉?佺被\', [640, 100], \'div-gpt-ad-1414399676656-0\').addService(googletag.pubads());

googletag.defineSlot(\'/2315836/Muisc-Channel_Right_160x350\', [160, 350], \'div-gpt-ad-1414401252795-0\').addService(googletag.pubads());

googletag.defineSlot(\'/2315836/Notice_Right_300x250\', [300, 250], \'div-gpt-ad-1414401341474-0\').addService(googletag.pubads());

googletag.defineSlot(\'/2315836/Music-Song_Bottom_300x250\', [640, 100], \'div-gpt-ad-1414481074453-0\').addService(googletag.pubads());
googletag.defineSlot(\'/2315836/Music-Song_Right_300x250\', [300, 250], \'div-gpt-ad-1414481115405-0\').addService(googletag.pubads());

googletag.defineSlot(\'/2315836/Collect-Detail_Right_300x250\', [300, 250], \'div-gpt-ad-1414481190531-0\').addService(googletag.pubads());
googletag.defineSlot(\'/2315836/Collect-Detail_Right2_300x250\', [300, 250], \'div-gpt-ad-1414393340166-0\').addService(googletag.pubads());

//googletag.pubads().enableSingleRequest();
googletag.pubads();// disabled ads combo request
googletag.enableServices();
});
</script>
	<!-- end -->

</head>
<body data-spm="3521865"><script>
with(document)with(body)with(insertBefore(createElement("script"),firstChild))setAttribute("exparams","category=&userid=&aplus&yunid=&&asid=AAB67HxWCMdQOp2NoNE=",id="tb-beacon-aplus",src=(location>"https"?"//s":"//a")+".tbcdn.cn/s/aplus_v2.js")
</script>



<div id="xiami-content"></div>
<div id="web_loading">Loading...</div>





<div id="header" data-spm="226669510" >
	<div class="primary">
		<div class="gap">
		<div class="wrapper">
			<table>
				<tr>
																				<td class="logo"><a href="http://www.xiami.com/" title="铏剧背闊充箰缃?(xiami.com) - 楂樺搧璐ㄩ煶涔? 鍙戠幇 鍒嗕韩">铏剧背闊充箰缃?(xiami.com) - 楂樺搧璐ㄩ煶涔? 鍙戠幇 鍒嗕韩</a></td>
										<td class="nav">
						<a class="bigtext " href="http://www.xiami.com/">鍙戠幇闊充箰</a>
						<a class="bigtext " href="http://www.xiami.com/space/lib-song">鎴戠殑闊充箰</a>
					</td>
					<td class="subnav">
						<a class="bigtext first " href="http://www.xiami.com/collect">绮鹃?夐泦</a>
						<a class="bigtext middle " target="_blank" href="http://www.xiami.com/radio">鐢靛彴</a>
						<a class="bigtext middle " href="http://i.xiami.com">闊充箰浜?</a>
						<script>
							document.write(\'<a class="bigtext last" href="http://yanchu.music.taobao.com/" target="_blank" style="zoom:1;position:relative;" onclick="goldlog.record(\\'/xiamipc.1.15\\',\\'\\',\\'event=click&from=xiaminav&userid=\'+_xiamiuser.split(\'"\')[0]+\'\\',\\'H46807199\\');">婕斿嚭<sup style="display:none;position:absolute;right:-13px;top:-6px;_top:1px;width:16px;height:18px;background:url(\\'http://img.xiami.net/static/img/common/sale.png\\') no-repeat"></sup></a>\');
						</script>
					</td>
					<td class="search">
						<div class="container">
							<form action="http://www.xiami.com/search" method="get" id="search">
								<input class="keyword" autocomplete="off" placeholder="闊充箰鎼滅储锛屾壘浜?..." name="key" />
								<input class="icon submit" type="submit" value="鎼滅储" />
								<input type="hidden" name="pos" value="1" />
							</form>
							<div class="auto_complete"></div>
						</div>
					</td>
										<td class="bigtext reg">
						<a href="http://www.xiami.com/member/register">鍏嶈垂娉ㄥ唽</a>
					</td>
					<td class="bigtext login">
						<a class="first" href="https://login.xiami.com/member/login">绔嬪嵆鐧诲綍</a>
						<a class="middle" href="" onclick="sinaLogin();return false;"><b class="icon weibo">weibo</b></a>
						<a class="last" href="" onclick="qqLogin();return false;"><b class="icon qq">qq</b></a>
					</td>
									</tr>
			</table>
			<div class="notify_popup">
				<div class="content">
					<div class="container"><p class="loading"></p></div>
					<b class="triangle"><i>鈼?</i>鈼?</b>
				</div>
			</div>
			<div class="user_popup">
				<div class="content">
					<ul>
						<li><a href="http://www.xiami.com/u/"><b class="icon home"></b>鎴戠殑涓婚〉</a></li>
						<li class="fence"></li>
						<li><a href="http://www.xiami.com/relation/following"><b class="icon relationship"></b>鍏虫敞 / 绮変笣</a></li>
						<li><a href="http://www.xiami.com/vip"><b class="icon vip"></b>VIP</a></li>
						<li><a href="http://www.xiami.com/account"><b class="icon account"></b>璐︽埛</a></li>
						<li><a href="http://www.xiami.com/property/myproperties"><b class="icon props"></b>閬撳叿</a></li>
						<li><a href="http://www.xiami.com/share"><b class="icon setting"></b>璁剧疆</a></li>
						<li class="fence"></li>
						<li><a href="" class="logout" onclick="return false;"><b class="icon logout"></b>閫?鍑?</a></li>
					</ul>
					<b class="triangle"><i>鈼?</i>鈼?</b>
				</div>
			</div>
		</div>
		</div>
	</div>
</div>
<div id="hidden_obj">
	<object data="/res/player/sdtos.swf?v=1451027577" type="application/x-shockwave-flash" width="1" height="1" id="trans" name="trans">
	    <param name="movie" value="/res/player/sdtos.swf?v=1451027577" />
	    <param name="quality" value="high" />
	    <param name="wmode" value="window" />
		<param name="allowScriptAccess" value="sameDomain" />
	</object>
</div>
<style type="text/css">
#wrapper .search_box{position:relative;}
.albumBlock_list ul li{ margin: 15px 7px 0 0;}
.artistBlock_list ul li{  margin: 0 27px 15px 0;}
.collectBlock_list ul li{margin: 10px 33px 10px 0;}
.track_list tr.same_group td {
  background-color:#fff4ed;
}
.track_list tr.same_group td.chkbox {
  border-left: 2px solid #f60;
}
.track_list a.slide_down,
.track_list a.slide_up {
  display:block;
  width:17px;
  height:17px;
  background-image:url(http://img.xiami.net/res/img/default/slide_group.gif);
  float:right;
  margin: 0 10px 0 0;
}
.track_list a.slide_down {
  background-position:0 0;
}
.track_list a.slide_down:hover {
  background-position:0 -17px;
}
.track_list a.slide_up {
  background-position:0 -34px !important;
}
.track_list a.slide_up:hover {
  background-position:0 -51px !important;
}
.vicos{background:url( http://img.xiami.net/res/img/default/verify_ico.gif) 100% 0 no-repeat; padding-right:18px;}
</style>
<script type="text/javascript">
$(function() {
  $(".track_list tr.same_group:first").show();

	$(".track_list a.slide_down").click(function(){
    	$(this).toggleClass("slide_down").toggleClass("slide_up");
		$(this).parents(\'tbody\').next("tbody.same_song_group").toggle().find(\'input[type=checkbox]\').attr(\'checked\',\'checked\');

	});
})
</script>

<div id="page" class="old">
	<div id="wrapper">
		<div class="title18_search">
	<h1>铏剧背闊充箰鎼滅储</h1>
	<div class="search_tab" data-spm="23309985">
		<ul>
			<li><a class="current" href="javascript:;" title=""><span>鍏ㄩ儴</span></a></li>
			<li><a href="http://www.xiami.com/search/song/?key=%E5%8F%8C%E6%88%AA%E6%A3%8D+%E5%91%A8%E6%9D%B0%E4%BC%A6" title="姝屾洸"><span>姝屾洸</span></a></li>
			<li><a href="http://www.xiami.com/search/album/?key=%E5%8F%8C%E6%88%AA%E6%A3%8D+%E5%91%A8%E6%9D%B0%E4%BC%A6" title="涓撹緫"><span>涓撹緫</span></a></li>
			<li><a href="http://www.xiami.com/search/artist/?key=%E5%8F%8C%E6%88%AA%E6%A3%8D+%E5%91%A8%E6%9D%B0%E4%BC%A6" title="鑹轰汉"><span>鑹轰汉</span></a></li>
			<li><a href="http://www.xiami.com/search/song-lyric/?key=%E5%8F%8C%E6%88%AA%E6%A3%8D+%E5%91%A8%E6%9D%B0%E4%BC%A6" title="姝岃瘝"><span>姝岃瘝</span></a></li>
			<li><a href="http://www.xiami.com/search/collect/?key=%E5%8F%8C%E6%88%AA%E6%A3%8D+%E5%91%A8%E6%9D%B0%E4%BC%A6" title="绮鹃?夐泦"><span>绮鹃?夐泦</span></a></li>
			<li><a href="http://www.xiami.com/song/tag/%E5%8F%8C%E6%88%AA%E6%A3%8D+%E5%91%A8%E6%9D%B0%E4%BC%A6" title=""><span>鏍囩</span></a></li>
		</ul>
	</div>
</div>
		<div class="more_cols clearfix">
			<div class="more_cols_left">
				<div class="more_cols_left_inner">
				<div class="search_box" data-spm="23309989">
					<form class="big_search_form" name="searchindex" id="" action="http://www.xiami.com/search" method="get" autocomplete="off" ONSUBMIT="search_focus();">
						<input class="big_search grey" type="text" id="search_text" name="key" title="鎼滅储鎮ㄦ劅鍏磋叮鐨勪笓杈?/姝屾洸/鑹轰汉"  value="鍙屾埅妫? 鍛ㄦ澃浼?" onfocus="search_focus(\'click\');" onblur="search_focus(\'blur\');" />
						<input class="big_search_bt" type="submit" value="鎼滅储" id="musicsearch" />
					</form>
                    <span style="position:absolute;left:0;bottom:10px;">澶у閮藉湪鍚櫨绫抽煶涔愪汉锛?<a href="/search?key=%E5%91%A8%E6%B7%B1&pos=1&from=searchbottom">鍛ㄦ繁</a></span>										<span class="hints">鏀寔鎷奸煶棣栧瓧姣嶆悳绱€?傚鎼滅储鈥滃垬寰峰崕鈥濊緭鍏モ?渓dh鈥濆嵆鍙??</span>
				</div>
				<input type="hidden" name="tour_name" value="鍙屾埅妫? 鍛ㄦ澃浼?" id="tour_name" />
											<div class="search_result">
														<!--song-->
										<div class="search_result_box" data-spm="23309997">
						<h5>姝屾洸</h5>
						<div class="result_main">
							<table class="track_list" cellspacing="0" cellpadding="0">
								<thead>
									<tr>
										<th class="chkbox">&nbsp;</th>
										<th class="song_name">姝屽悕</th>
										<th class="song_artist">鑹轰汉</th>
										<th class="song_album">鎵?灞炰笓杈?</th>
										<th class="song_act">&nbsp;</th>
									</tr>
								</thead>
								<tbody>
																		<tr class="same_group group_first ">
										<td class="chkbox">
											<input  DISABLED="disable" type="checkbox"  value="81363" name="recommendids" />
										</td>
										<td class="song_name">
																						<a href="javascript:;" class="slide_down" title="璇ヨ壓浜烘紨鍞辩殑鍏朵粬鐗堟湰"></a>
																						<a target="_blank" href="http://www.xiami.com/song/81363" title="鍙屾埅妫?"><b class="key_red">鍙屾埅妫?</b></a>
																																											</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/1260" title="Jay Chou">
												<b class="key_red">鍛ㄦ澃浼?</b>											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/6644" title="Initial J">銆奍nitial J銆?</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'81363\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'81363\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(81363,3);" title="">娣诲姞鏍囩</a>
</span>
</div></div>																					</td>
									</tr>
																		<tbody class="same_song_group" style="display:none;">
																				<tr class=\'same_group\' >
											<td class="chkbox">
												<input  DISABLED="disable" type="checkbox"  value="376070" name="recommendids" />
											</td>
											<td class="song_name">
												<a target="_blank" href="http://www.xiami.com/song/376070" title="鍙屾埅妫?"><b class="key_red">鍙屾埅妫?</b></a>
																																			</td>
											<td class="song_artist">
												<a target="_blank" href="http://www.xiami.com/artist/1260" title="Jay Chou">
													<b class="key_red">鍛ㄦ澃浼?</b>												</a>
											</td>
											<td class="song_album">
												<a target="_blank" href="http://www.xiami.com/album/6655" title="Fantasy">銆婅寖鐗硅タ銆?</a>
											</td>
											<td class="song_act">
												<div class="song_do" style="width:170px;">
																										<a class="song_digg" href="javascript:void(0)" title="鍒嗕韩" onclick="recommend(\'376070\',\'32\')">鍒嗕韩</a>
													<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'376070\');">娣诲姞鍒?</a>
																																								<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(376070,3);" title="">娣诲姞鏍囩</a>
</span>
</div>																									</div>
											</td>
										</tr>
																			</tbody>

																<tr class=" bg_grey">
										<td class="chkbox">
											<input  DISABLED="disable" type="checkbox"  value="81422" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/81422" title="鍙屽垁 / 鍙屾埅妫? / 榫欐嫵(Live)">鍙屽垁 / <b class="key_red">鍙屾埅妫?</b> / 榫欐嫵(Live)</a>
																																											</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/1260" title="Jay Chou">
												<b class="key_red">鍛ㄦ澃浼?</b>											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/6647" title="2004鏃犱笌浼︽瘮婕斿敱浼?">銆?2004鏃犱笌浼︽瘮婕斿敱浼氥??</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'81422\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'81422\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(81422,3);" title="">娣诲姞鏍囩</a>
</span>
</div></div>																					</td>
									</tr>

																<tr class="same_group group_first ">
										<td class="chkbox">
											<input  DISABLED="disable" type="checkbox"  value="81482" name="recommendids" />
										</td>
										<td class="song_name">
																						<a href="javascript:;" class="slide_down" title="璇ヨ壓浜烘紨鍞辩殑鍏朵粬鐗堟湰"></a>
																						<a target="_blank" href="http://www.xiami.com/song/81482" title="鍙屾埅妫? (Live)"><b class="key_red">鍙屾埅妫?</b> (Live)</a>
																																											</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/1260" title="Jay Chou">
												<b class="key_red">鍛ㄦ澃浼?</b>											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/6651" title="The One 婕斿敱浼?">銆奣he One 婕斿敱浼氥??</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'81482\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'81482\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(81482,3);" title="">娣诲姞鏍囩</a>
</span>
</div></div>																					</td>
									</tr>
																		<tbody class="same_song_group" style="display:none;">
																				<tr class=\'same_group\' >
											<td class="chkbox">
												<input  DISABLED="disable" type="checkbox"  value="1769998718" name="recommendids" />
											</td>
											<td class="song_name">
												<a target="_blank" href="http://www.xiami.com/song/1769998718" title="鍙屾埅妫? (Live)"><b class="key_red">鍙屾埅妫?</b> (Live)</a>
																																			</td>
											<td class="song_artist">
												<a target="_blank" href="http://www.xiami.com/artist/1260" title="Jay Chou">
													<b class="key_red">鍛ㄦ澃浼?</b>												</a>
											</td>
											<td class="song_album">
												<a target="_blank" href="http://www.xiami.com/album/422597" title="The Era 2010 瓒呮椂浠ｆ紨鍞变細">銆奣he Era 2010 瓒呮椂浠ｆ紨鍞变細銆?</a>
											</td>
											<td class="song_act">
												<div class="song_do" style="width:170px;">
																										<a class="song_digg" href="javascript:void(0)" title="鍒嗕韩" onclick="recommend(\'1769998718\',\'32\')">鍒嗕韩</a>
													<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1769998718\');">娣诲姞鍒?</a>
																																								<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1769998718,3);" title="">娣诲姞鏍囩</a>
</span>
</div>																									</div>
											</td>
										</tr>
																				<tr class=\'same_group\' >
											<td class="chkbox">
												<input  DISABLED="disable" type="checkbox"  value="3516768" name="recommendids" />
											</td>
											<td class="song_name">
												<a target="_blank" href="http://www.xiami.com/song/3516768" title="鍙屾埅妫? (Live)"><b class="key_red">鍙屾埅妫?</b> (Live)</a>
																																			</td>
											<td class="song_artist">
												<a target="_blank" href="http://www.xiami.com/artist/1260" title="Jay Chou">
													<b class="key_red">鍛ㄦ澃浼?</b>												</a>
											</td>
											<td class="song_album">
												<a target="_blank" href="http://www.xiami.com/album/33354" title="2007涓栫晫宸″洖婕斿敱浼?">銆?2007涓栫晫宸″洖婕斿敱浼氥??</a>
											</td>
											<td class="song_act">
												<div class="song_do" style="width:170px;">
																										<a class="song_digg" href="javascript:void(0)" title="鍒嗕韩" onclick="recommend(\'3516768\',\'32\')">鍒嗕韩</a>
													<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'3516768\');">娣诲姞鍒?</a>
																																								<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(3516768,3);" title="">娣诲姞鏍囩</a>
</span>
</div>																									</div>
											</td>
										</tr>
																			</tbody>

																<tr class=" bg_grey">
										<td class="chkbox">
											<input  DISABLED="disable" type="checkbox"  value="1773859333" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/1773859333" title="鍙屾埅妫? / 鎯婂徆鍙? (Live)"><b class="key_red">鍙屾埅妫?</b> / 鎯婂徆鍙? (Live)</a>
																																											</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/7169" title="Various Artists">
												缇ゆ槦(<b class="key_red">鍛ㄦ澃浼?</b>)											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/1020552829" title="2015姹熻嫃鍗鏂板勾婕斿敱浼?">銆?2015姹熻嫃鍗鏂板勾婕斿敱浼氥??</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'1773859333\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1773859333\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1773859333,3);" title="">娣诲姞鏍囩</a>
</span>
</div></div>																					</td>
									</tr>

																<tr class=" ">
										<td class="chkbox">
											<input checked="checked" type="checkbox"  value="1774315616" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/1774315616" title="鍙屾埅妫? Remix"><b class="key_red">鍙屾埅妫?</b> Remix</a>
																																											</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/27465173" title="Panta.Q">
												Panta.Q											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/1431888513" title="Panta.Q">銆奝anta.Q銆?</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_play" href="javascript:void(0)" title="璇曞惉" onclick="play(\'1774315616\');"><span>璇曞惉</span></a>
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'1774315616\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1774315616\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<a class="song_download" href="javascript:void(0)" title="涓嬭浇" onclick="xm_download(\'1774315616\');"><span>涓嬭浇</span></a>
<a class="song_tel" href="javascript:void(0)" onclick="showDialog(\'/music/send/id/1774315616\');" title="鍙戦?佸埌">鍙戦?佸埌</a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1774315616,3);" title="">娣诲姞鏍囩</a>
<a class="toplayer" href="http://www.xiami.com/widget/isingle?sid=1774315616" title="">杞创鍒板叾瀹冪綉绔?</a></span>
</div></div>																					</td>
									</tr>

																<tr class=" bg_grey">
										<td class="chkbox">
											<input checked="checked" type="checkbox"  value="1772339075" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/1772339075" title="鍙屾埅妫? (Live)"><b class="key_red">鍙屾埅妫?</b> (Live)</a>
																																											</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/1681385290" title="Celebrity聽Battle">
												鍏ㄨ兘鏄熸垬(榫氱惓濞?)											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/484503013" title="绗叚鏈? 娴佽鑺傚涔嬪">銆婄鍏湡 娴佽鑺傚涔嬪銆?</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_play" href="javascript:void(0)" title="璇曞惉" onclick="play(\'1772339075\');"><span>璇曞惉</span></a>
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'1772339075\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1772339075\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<a class="song_download" href="javascript:void(0)" title="涓嬭浇" onclick="xm_download(\'1772339075\');"><span>涓嬭浇</span></a>
<a class="song_tel" href="javascript:void(0)" onclick="showDialog(\'/music/send/id/1772339075\');" title="鍙戦?佸埌">鍙戦?佸埌</a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1772339075,3);" title="">娣诲姞鏍囩</a>
<a class="toplayer" href="http://www.xiami.com/widget/isingle?sid=1772339075" title="">杞创鍒板叾瀹冪綉绔?</a></span>
</div></div>																					</td>
									</tr>

																<tr class=" ">
										<td class="chkbox">
											<input  DISABLED="disable" type="checkbox"  value="45048" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/45048" title="鍙屾埅妫?"><b class="key_red">鍙屾埅妫?</b></a>
																																											</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/765" title="娼橀暱姹?">
												娼橀暱姹?											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/3661" title="鐢蜂汉40涓?鏋濊姳">銆婄敺浜?40涓?鏋濊姳銆?</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'45048\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'45048\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(45048,3);" title="">娣诲姞鏍囩</a>
</span>
</div></div>																					</td>
									</tr>

																<tr class=" bg_grey">
										<td class="chkbox">
											<input  DISABLED="disable" type="checkbox"  value="1774615988" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/1774615988" title="鍙屾埅妫? (Live)"><b class="key_red">鍙屾埅妫?</b> (Live)</a>
																																	<a class="show_zhcn" href="http://www.xiami.com/song/1774615988" title="">閫夋嫨瀵煎笀: 鍛ㄦ澃浼?</a>
																																</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/119672" title="The Voice of China">
												涓浗濂藉０闊?(鏌崇晠婧?)											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/2100180958" title="The Voice of China, Season 4: Blind Auditions 3">銆婄鍥涘 鐩查?夌涓夋湡銆?</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'1774615988\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1774615988\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1774615988,3);" title="">娣诲姞鏍囩</a>
</span>
</div></div>																					</td>
									</tr>

																<tr class=" ">
										<td class="chkbox">
											<input  DISABLED="disable" type="checkbox"  value="1774525832" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/1774525832" title="鍙屾埅妫? (Live)"><b class="key_red">鍙屾埅妫?</b> (Live)</a>
																																	<a class="show_zhcn" href="http://www.xiami.com/song/1774525832" title="">閫夋嫨瀵煎笀: 鍛ㄦ澃浼?</a>
																																</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/119672" title="The Voice of China">
												涓浗濂藉０闊?(闄堟绔?)											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/1837535388" title="The Voice of China, Season 4: Blind Auditions 1">銆婄鍥涘 鐩查?夌涓?鏈熴??</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'1774525832\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1774525832\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1774525832,3);" title="">娣诲姞鏍囩</a>
</span>
</div></div>																					</td>
									</tr>

																<tr class=" bg_grey">
										<td class="chkbox">
											<input checked="checked" type="checkbox"  value="1772014958" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/1772014958" title="瀹滃浜鸿?嶅弻鎴">瀹滃浜鸿??<b class="key_red">鍙屾埅妫?</b></a>
																																	<a class="show_zhcn" href="http://www.xiami.com/song/1772014958" title="">鍛ㄦ澃浼︺?婂弻鎴銆?</a>
																																</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/90361" title="琛ｆ箍">
												琛ｆ箍											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/1073618388" title="鑽℃钉蹇冪伒鐨勫彂鐑т箣浣?">銆婂疁瀹惧甯傚湡鎽囬噾鏇层??</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_play" href="javascript:void(0)" title="璇曞惉" onclick="play(\'1772014958\');"><span>璇曞惉</span></a>
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'1772014958\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1772014958\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<a class="song_download" href="javascript:void(0)" title="涓嬭浇" onclick="xm_download(\'1772014958\');"><span>涓嬭浇</span></a>
<a class="song_tel" href="javascript:void(0)" onclick="showDialog(\'/music/send/id/1772014958\');" title="鍙戦?佸埌">鍙戦?佸埌</a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1772014958,3);" title="">娣诲姞鏍囩</a>
<a class="toplayer" href="http://www.xiami.com/widget/isingle?sid=1772014958" title="">杞创鍒板叾瀹冪綉绔?</a></span>
</div></div>																					</td>
									</tr>

																<tr class=" ">
										<td class="chkbox">
											<input  DISABLED="disable" type="checkbox"  value="1774202630" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/1774202630" title="鍙屾埅妫? (Demo)"><b class="key_red">鍙屾埅妫?</b> (Demo)</a>
																																											</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/1260" title="Jay Chou">
												<b class="key_red">鍛ㄦ澃浼?</b>											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/329607612" title="ARIA J III MP3 Player 512MB 闄愰噺鏅堕捇鐗堥檮璧犻煶棰?">銆奐 III銆?</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'1774202630\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1774202630\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1774202630,3);" title="">娣诲姞鏍囩</a>
</span>
</div></div>																					</td>
									</tr>

																<tr class=" bg_grey">
										<td class="chkbox">
											<input checked="checked" type="checkbox"  value="1775348896" name="recommendids" />
										</td>
										<td class="song_name">
																						<a target="_blank" href="http://www.xiami.com/song/1775348896" title="Jay Chou Ft.Skrillex - 鍙岃妭妫岯angarang (DJ Harry Mashup)">Jay Chou Ft.Skrillex - 鍙岃妭妫岯angarang (DJ Harry Mashup)</a>
																																	<a class="show_zhcn" href="http://www.xiami.com/song/1775348896" title="">褰撳懆鏉颁鸡鍙屾埅妫嶉亣涓夿angarang-"skrillex"姣棤杩濆拰鎰?</a>
																																</td>
										<td class="song_artist">
											<a target="_blank" href="http://www.xiami.com/artist/1736157779" title="DJHarry">
												DJHarry											</a>
										</td>
										<td class="song_album">
																						<a target="_blank" href="http://www.xiami.com/album/2100242910" title="褰撳懆鏉颁鸡鍙屾埅妫嶉亣涓夿angarang-"skrillex"姣棤杩濆拰鎰?">銆?<b class="key_red">鍛ㄦ澃浼?</b><b class="key_red">鍙屾埅妫?</b>閬囦笂Bangarang-"skrillex"姣棤杩濆拰鎰熴??</a>
																					</td>
										<td class="song_act">
																							<div class="song_do" style="width:170px;_width:180px;">
<a class="song_play" href="javascript:void(0)" title="璇曞惉" onclick="play(\'1775348896\');"><span>璇曞惉</span></a>
<a class="song_digg" href="javascript:void(0)" title="鎺ㄨ崘" onclick="recommend(\'1775348896\',\'32\')"><span>鎺ㄨ崘</span></a>
<a class="song_toclt" href="javascript:void(0)" title="娣诲姞鍒扮簿閫夐泦" onclick="collect(\'1775348896\');"><span>娣诲姞鍒癮m绮鹃?夐泦</span></a>
<a class="song_download" href="javascript:void(0)" title="涓嬭浇" onclick="xm_download(\'1775348896\');"><span>涓嬭浇</span></a>
<a class="song_tel" href="javascript:void(0)" onclick="showDialog(\'/music/send/id/1775348896\');" title="鍙戦?佸埌">鍙戦?佸埌</a>
<div class="song_menu">
<a class="song_more" href="javascript:void(0)" title="">鏇村</a>
<span class="song_menu_drop">
<em></em>
<a href="javascript:;" onclick="tag(1775348896,3);" title="">娣诲姞鏍囩</a>
<a class="toplayer" href="http://www.xiami.com/widget/isingle?sid=1775348896" title="">杞创鍒板叾瀹冪綉绔?</a></span>
</div></div>																					</td>
									</tr>

															</tbody>

							</table>
						</div>
						<div class="chapter_ctrl cd_count">
							<div class="ctrl_play">
								<a onclick="selectAll(\'recommendids\')" title="" href="javascript:void(0)" class="bt_choose">
									<span>鍏ㄩ??</span>
								</a>
								<a title="" onclick="inverse(\'recommendids\');" href="javascript:void(0);" class="bt_choose">
									<span>鍙嶉??</span>
								</a>
								<a onclick="playsongs(\'recommendids\');" title="" href="javascript:void(0);" class="bt_play">
									<span>鎾斁閫変腑姝屾洸</span>
								</a>
							</div>
						</div>
												<span class="y_more">
							<a href="http://www.xiami.com/search/song?key=%E5%8F%8C%E6%88%AA%E6%A3%8D+%E5%91%A8%E6%9D%B0%E4%BC%A6" title="">鏇村姝屾洸(16)</a>
						</span>
											</div>
										<!--radio-->
										<!--album-->
										<div class="search_result_box" data-spm="23310001">
						<h5>涓撹緫</h5>
						<div class="result_main">
							<div class="albumBlock_list" >
								<ul class="clearfix">

									<style>
.album_item100_block .album_rank{position:relative;height:12px;margin:10px 0 10px 5px;padding-left:50px;color:#999;background:url(\'http://img.xiami.net/res/v3/img/star4_v3.png\') no-repeat 0 2px;vertical-align:middle;}
.album_item100_block .album_rank span{position:absolute;height:12px;left:0;top:0;background:url(\'http://img.xiami.net/res/v3/img/star4_v3.png\') no-repeat 0 -8px;text-indent:-9999px;}
.album_item100_block .album_rank em{float:left;margin-left:5px;font:normal 10px tahoma;color:#F60;vertical-align:middle;}
.album_item100_block .name {height:45px !important;}
</style>

																	<li>
										<div class="album_item100_block">
											<p class="cover">
												<a class="CDcover100" href="http://www.xiami.com/album/2100242910" title="">
													<img src="http://img.xiami.net/images/album/img79/1736157779/21002429101448868012_1.jpg" width="100" height="100" alt="" />
												</a>
																							</p>
											<p class="name">
												<a class="song" href="http://www.xiami.com/album/2100242910" title="鍛ㄦ澃浼﹀弻鎴閬囦笂Bangarang-"skrillex"姣棤杩濆拰鎰?" >
													<b class="key_red">鍛ㄦ澃浼?</b><b class="key_red">鍙屾埅妫?</b>閬囦笂Ba...
																									<span class="album_name">(褰撳懆鏉颁鸡鍙屾埅妫嶉亣涓夿...)</span>
																								</a>
												<a class="singer" href="http://www.xiami.com/artist/1736157779" title="DJHarry">DJHarry</a>
											</p>
											<p class="album_rank clearfix">
												<span style="width:0px;">鎬讳綋璇勫垎</span>
												<em>0.0</em>
											</p>
											<p class="year">2015-11-30</p>
										</div>
									</li>
																	</ul>
							</div>
						</div>
											</div>
										<!--artist-->
										<div class="search_result_box search_result_box_artist" data-spm="226668882">
						<h5>鑹轰汉</h5>
						<div class="result_main">
							<div class="artistBlock_list">
								<ul>
																		<li class="hor-list-item m15">
										<div class="artist_item100_block">
											<p class="buddy">
												<a target="_blank" class="artist100" href="http://www.xiami.com/artist/1260" title="鍛ㄦ澃浼?">
													<img  src="http://img.xiami.net/images/artistlogo/68/13161013044368_1.jpg" width="100" height="100" alt="" />
												</a>
											</p>
											<p class="name">
												<a  class="title" href="http://www.xiami.com/artist/1260" title="Jay Chou">
													<strong><b class="key_red">鍛ㄦ澃浼?</b>
																												<span class="singer_names">(Jay Chou)</span>
																											</strong>
												</a> <b class="ico_radio ele_inline mah"><a title="鎾斁鍛ㄦ澃浼︾殑鐢靛彴" href="http://www.xiami.com/radio/play/type/5/oid/1260" target="_blank">鐢靛彴</a></b>
																								<span class="singer_region" title="Taiwan 鍙版咕">Taiwan 鍙版咕</span>
																							</p>
											<!--<p class="counts">27寮犱笓杈? | 1418114浣嶇矇涓?</p>
										-->
									</div>
								</li>
																	<li class="hor-list-item m15">
										<div class="artist_item100_block">
											<p class="buddy">
												<a target="_blank" class="artist100" href="http://www.xiami.com/artist/27465173" title="Panta.Q">
													<img  src="http://img.xiami.net/images/artistlogo/42/14321015924142_1.jpg" width="100" height="100" alt="" />
												</a>
											</p>
											<p class="name">
												<a  class="title" href="http://www.xiami.com/artist/27465173" title="">
													<strong>Panta.Q
																											</strong>
												</a> <b class="ico_radio ele_inline mah"><a title="鎾斁Panta.Q鐨勭數鍙?" href="http://www.xiami.com/radio/play/type/5/oid/27465173" target="_blank">鐢靛彴</a></b>
																								<span class="singer_region" title="China 涓浗澶ч檰">China 涓浗澶ч檰</span>
																							</p>
											<!--<p class="counts">1寮犱笓杈? | 109浣嶇矇涓?</p>
										-->
									</div>
								</li>
																	<li class="hor-list-item m15">
										<div class="artist_item100_block">
											<p class="buddy">
												<a target="_blank" class="artist100" href="http://www.xiami.com/artist/1681385290" title="鍏ㄨ兘鏄熸垬">
													<img  src="http://img.xiami.net/images/artistlogo/56/13821702744756_1.png" width="100" height="100" alt="" />
												</a>
											</p>
											<p class="name">
												<a  class="title" href="http://www.xiami.com/artist/1681385290" title="Celebrity聽Battle">
													<strong>鍏ㄨ兘鏄熸垬
																												<span class="singer_names">(Celebrity聽...)</span>
																											</strong>
												</a> <b class="ico_radio ele_inline mah"><a title="鎾斁鍏ㄨ兘鏄熸垬鐨勭數鍙?" href="http://www.xiami.com/radio/play/type/5/oid/1681385290" target="_blank">鐢靛彴</a></b>
																								<span class="singer_region" title="China 涓浗澶ч檰">China 涓浗澶ч檰</span>
																							</p>
											<!--<p class="counts">12寮犱笓杈? | 3051浣嶇矇涓?</p>
										-->
									</div>
								</li>
																	<li class="hor-list-item m15">
										<div class="artist_item100_block">
											<p class="buddy">
												<a target="_blank" class="artist100" href="http://www.xiami.com/artist/765" title="娼橀暱姹?">
													<img  src="http://img.xiami.net/images/artistlogo/45/13819870176045_1.jpg" width="100" height="100" alt="" />
												</a>
											</p>
											<p class="name">
												<a  class="title" href="http://www.xiami.com/artist/765" title="">
													<strong>娼橀暱姹?
																											</strong>
												</a> <b class="ico_radio ele_inline mah"><a title="鎾斁娼橀暱姹熺殑鐢靛彴" href="http://www.xiami.com/radio/play/type/5/oid/765" target="_blank">鐢靛彴</a></b>
																								<span class="singer_region" title="China 涓浗澶ч檰">China 涓浗澶ч檰</span>
																							</p>
											<!--<p class="counts">1寮犱笓杈? | 361浣嶇矇涓?</p>
										-->
									</div>
								</li>
																	<li class="hor-list-item m15">
										<div class="artist_item100_block">
											<p class="buddy">
												<a target="_blank" class="artist100" href="http://www.xiami.com/artist/90361" title="琛ｆ箍">
													<img  src="http://img.xiami.net/images/artistlogo/7/14342742345507_1.jpg" width="100" height="100" alt="" />
												</a>
											</p>
											<p class="name">
												<a  class="title" href="http://www.xiami.com/artist/90361" title="">
													<strong>琛ｆ箍
																											</strong>
												</a> <b class="ico_radio ele_inline mah"><a title="鎾斁琛ｆ箍鐨勭數鍙?" href="http://www.xiami.com/radio/play/type/5/oid/90361" target="_blank">鐢靛彴</a></b>
																								<span class="singer_region" title="China 涓浗澶ч檰">China 涓浗澶ч檰</span>
																							</p>
											<!--<p class="counts">10寮犱笓杈? | 9469浣嶇矇涓?</p>
										-->
									</div>
								</li>
																	<li class="hor-list-item m15">
										<div class="artist_item100_block">
											<p class="buddy">
												<a target="_blank" class="artist100" href="http://www.xiami.com/artist/1736157779" title="DJHarry">
													<img  src="http://img.xiami.net/images/artistlogo/91/14488681397891_1.jpg" width="100" height="100" alt="" />
												</a>
											</p>
											<p class="name">
												<a  class="title" href="http://www.xiami.com/artist/1736157779" title="DJHarry">
													<strong>DJHarry
																												<span class="singer_names">(DJHarry)</span>
																											</strong>
												</a> <b class="ico_radio ele_inline mah"><a title="鎾斁DJHarry鐨勭數鍙?" href="http://www.xiami.com/radio/play/type/5/oid/1736157779" target="_blank">鐢靛彴</a></b>
																								<span class="singer_region" title="China 涓浗澶ч檰">China 涓浗澶ч檰</span>
																							</p>
											<!--<p class="counts">13寮犱笓杈? | 84浣嶇矇涓?</p>
										-->
									</div>
								</li>
																	<li class="hor-list-item m15">
										<div class="artist_item100_block">
											<p class="buddy">
												<a target="_blank" class="artist100" href="http://www.xiami.com/artist/1527700959" title="寰愭皬">
													<img  src="http://img.xiami.net/images/artistlogo/35/14277017888235_1.jpg" width="100" height="100" alt="" />
												</a>
											</p>
											<p class="name">
												<a  class="title" href="http://www.xiami.com/artist/1527700959" title="">
													<strong>寰愭皬
																											</strong>
												</a> <b class="ico_radio ele_inline mah"><a title="鎾斁寰愭皬鐨勭數鍙?" href="http://www.xiami.com/radio/play/type/5/oid/1527700959" target="_blank">鐢靛彴</a></b>
																								<span class="singer_region" title="China 涓浗澶ч檰">China 涓浗澶ч檰</span>
																							</p>
											<!--<p class="counts">4寮犱笓杈? | 22浣嶇矇涓?</p>
										-->
									</div>
								</li>
															</ul>
						</div>
					</div>
									</div>
								<!--collect-->
								<div class="search_result_box search_result_box_collect" data-spm="23310005">
					<h5>绮鹃?夐泦</h5>
					<div class="result_main">
						<!--block-->
						<div class="collectBlock_list">
							<ul class="clearfix">						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/48411282" title="杞溂澶氬勾鍛ㄦ澃浼?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/282/82/48411282_1429607689_xmxV_1.jpeg"  alt="" /></span></p>
								<p class="name">杞溂澶氬勾<b class="key_red">鍛ㄦ澃浼?</b></p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'48411282\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/5020716" title="">Backer</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/41591499" title="鍐嶆瀵绘壘鍛ㄦ澃浼︺??">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/499/99/41591499_1424099664_8pK5_1.jpg"  alt="" /></span></p>
								<p class="name">鍐嶆瀵绘壘<b class="key_red">鍛ㄦ澃浼?</b>銆?</p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'41591499\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/7800081" title="">鍒樿瘲蹇?</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/47696483" title="鍐嶈鍛ㄦ澃浼︺??">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/483/83/47696483_5525d65511cd8_WEXi_1428543061_1.jpg"  alt="" /></span></p>
								<p class="name">鍐嶈<b class="key_red">鍛ㄦ澃浼?</b>銆?</p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'47696483\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/47681882" title="">imyours_youa</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/45859262" title="鍛ㄦ澃浼︿綔鍝侀泦锛氳法瓒婃椂浠ｏ紝鎵嶅崕妯孩">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/262/62/45859262_1440515329_meu4_1.jpg"  alt="" /></span></p>
								<p class="name"><b class="key_red">鍛ㄦ澃浼?</b>浣滃搧闆嗭細璺ㄨ秺鏃朵唬锛屾墠鍗庢í婧?</p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'45859262\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/6501952" title="">liminray</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/48461648" title="鍛ㄦ澃浼?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/648/48/48461648_1429175857_A0pB_1.jpg"  alt="" /></span></p>
								<p class="name"><b class="key_red">鍛ㄦ澃浼?</b></p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'48461648\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/3815524" title="">J</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/48454226" title="鍛ㄦ澃浼?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/226/26/48454226_1429162518_bejX_1.jpg"  alt="" /></span></p>
								<p class="name"><b class="key_red">鍛ㄦ澃浼?</b></p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'48454226\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/6274986" title="">Yannn</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/48438875" title="鍛ㄦ澃浼?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/875/75/48438875_55af01a4f3f88_n9Dd_1437532580_1.jpg"  alt="" /></span></p>
								<p class="name"><b class="key_red">鍛ㄦ澃浼?</b></p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'48438875\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/19547977" title="">鑷範瀹よ祫娣辨偅鑰?</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/48509931" title="鍛ㄦ澃浼?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/931/31/48509931_1429427596_XV2r_1.jpeg"  alt="" /></span></p>
								<p class="name"><b class="key_red">鍛ㄦ澃浼?</b></p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'48509931\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/1027827" title="">鍚歌楝糆ther</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/48415708" title="鍛ㄦ澃鍊?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/708/8/48415708_1438158418_k2sb_1.jpg"  alt="" /></span></p>
								<p class="name">鍛ㄦ澃鍊?</p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'48415708\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/23784835" title="">鍗楀北</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/39093384" title="鍛ㄦ澃浼?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/384/84/39093384_1419790614_wVwu_1.jpg"  alt="" /></span></p>
								<p class="name"><b class="key_red">鍛ㄦ澃浼?</b></p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'39093384\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/45408722" title="">鈺? L 涓秌</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/48456268" title="鍛ㄦ澃浼?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/268/68/48456268_1429165497_9MM6_1.jpg"  alt="" /></span></p>
								<p class="name"><b class="key_red">鍛ㄦ澃浼?</b></p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'48456268\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/49260450" title="">鐚収鎱2009</a>


								</p>
							</div>
						</li>
						<li>
							<div class="collect_item100_block">
							<a class="info"  href="http://www.xiami.com/collect/38416183" title="鍛ㄦ澃浼?">
								<p class="cover"><span><img src="http://img.xiami.net/images/collect/183/83/38416183_1418397754_a67k_1.jpg"  alt="" /></span></p>
								<p class="name"><b class="key_red">鍛ㄦ澃浼?</b></p>
								</a>
								<b class="ico_cd ele_inline"><a title="" onclick="playcollect(\'38416183\')" href="javascript:void(0)">璇曞惉</a></b>

								<p class="author">by<a href="http://www.xiami.com/u/44791321" title="">wuhai19930820</a>


								</p>
							</div>
						</li>
     </ul>
						</div>
						<!--block-->

						<!--page end-->
					</div>
										<span class="y_more">
						<a href="http://www.xiami.com/search/collect?key=%E5%8F%8C%E6%88%AA%E6%A3%8D+%E5%91%A8%E6%9D%B0%E4%BC%A6" title="">鏇村绮鹃?夐泦(100)</a>
					</span>
									</div>
							</div>
					</div>
		</div>
		<div class="chnl_right" data-spm="23309993">

			<div class="add2xiami_bt">
				<p>
					<a href="http://www.xiami.com/wiki/addalbum" title="">娣诲姞铏剧背杩樻病鏈夌殑涓撹緫</a>
				</p>
				<p>
					<a href="http://www.xiami.com/wiki/addartist" title="">娣诲姞铏剧背杩樻病鏈夌殑鑹轰汉</a>
				</p>
			</div>

						<div class="add2xiami_bt">
				<p>
					<a href="http://www.xiami.com/song/tag/鍙屾埅妫? 鍛ㄦ澃浼?" title="">鏌ョ湅鏍囩涓哄弻鎴 鍛ㄦ澃浼︾殑姝屾洸</a>
				</p>
				<p>
					<a href="http://www.xiami.com/artist/tag/鍙屾埅妫? 鍛ㄦ澃浼?" title="">鏌ョ湅鏍囩涓哄弻鎴 鍛ㄦ澃浼︾殑鑹轰汉</a>
				</p>
			</div>

			<div id="search_relate_musician" style="display:none;">
				<h4>浣犲彲鑳戒細鎰熷叴瓒ｇ殑闊充箰浜?</h4>
				<div class="common_sec">
					<ul id="related_musician"></ul>
				</div>
			</div>
			<div id="hot_events_show" class="blank30">
				<script>show_hot_events(\'search-index\');  //鎺ㄨ崘涓撻灞曠ず</script>
			</div>
		</div>

	</div>
</div>
<!--content end-->
</div>




<script language="javascript">
var matched_artist_id = \'0\';
var home_site = \'http://www.xiami.com\';
var subject_type = \'\';
var subject_artist_id = \'\';
var subject_album_id = \'\';


$(document).ready(function(){
	if(subject_artist_id!=\'\' && subject_type==\'artist\'){
		$.getJSON(\'/count/getplaycount\',{\'id\':subject_artist_id,\'type\':\'artist\'},function(data){
			$(\'#play_count_num\').html(data.plays);
		});
		$.getJSON(\'/search/search-subject\',{\'id\':subject_artist_id,\'type\':\'artist\'},function(data){
			var content = \'\';
			$(\'#artist_musicians\').html(data.musicians);
			$(\'#artist_comment_num\').html(data.count_comment);
			$(\'#artist_hot_play\').click(function(){
				   play(data.hotsongs);
			});
			if(data.styles){
	        	$.each(data.styles,function(i,styles){
	        		content += \'<a href="/genre/detail/\';
	        		if(styles.same_genre!=0){
	        			content += \'gid/\'+styles.same_genre;
	        		}else{
	        			content += \'sid/\'+styles.style_id;
	        		}
	        		content += \'?from=searchsubject" target="_blank">\';
	        		if(styles.name_cn){
	        			content += styles.name_cn+"&nbsp;";
	        		}
	        		content += styles.name+\'</a>,\';
	        	});
	        	$(\'#artist_styles_name\').html(\'椋庢牸锛?\');
	        	$(\'#artist_styles\').append(content.slice(0,-1));
			}
		});
	}
	if(subject_album_id!=\'\' && subject_type==\'album\'){
		$.getJSON(\'/search/search-subject\',{\'id\':subject_album_id,\'type\':\'album\'},function(data){
			$(\'#album_comment_num\').html(data.count_comment);
			$(\'#album_collect_num\').html(data.collects);
			$(\'#album_category\').html(data.categoryName);
			$(\'#album_grade\').html(data.gradeStat.grade);
			$(\'#album_width\').width(data.gradeStat.width);
			$(\'#album_grade_count\').html(data.gradeStat.grade_count);
		});
	}

    $.getJSON(\'/ajax/rec-musician\',{artist_id:matched_artist_id},function(data) {
        var related_musician_count = 0;
        $.each(data,function(i,musician){
            related_musician_count++;
            var content = \'<li><div class="group_item55_side">\';
            content += \'<p class="cover"><a href="\'+home_site+\'/artist/\'+musician.artist_id+\'" title="\'+musician.name+\'"><img src="\'+(musician.logo?musician.logo:\'res/img/default/cd55.gif\')+\'"  width="55" height="55"/></a></p>\';
            content += \'<strong><a href="\'+home_site+\'/artist/\'+musician.artist_id+\'" title="\'+musician.name+\'" name_card="\'+musician.musician_uid+\'" >\'+musician.name+\'</a></strong>\';
            content += \' <a href="http://i.xiami.com" target="_blank" title="闊充箰浜?" style="display:inline" ><i class="G_ico12 icon_v12"></i></a>\';
            content += \'<p class="count count_item">\'+musician.count_likes+\'浣嶇矇涓?</p></div></li>\';
            $(\'#related_musician\').append(content);
        });
        if(related_musician_count>0){
            $(\'#search_relate_musician\').show();
        }
    });



	$(".album .image").hover(function(){

		$(this).find(\'i\').show();
		$(this).find(\'b\').show();
		$(this).find(\'dl\').show();

		$(this).find(\'dl\').hover(function(){
			$(this).find(\'dd\').show();
		},function(){
			$(this).find(\'dd\').hide();
		});

	},function(){

		$(this).find(\'i\').hide();
		$(this).find(\'b\').hide();
		$(this).find(\'dl\').hide();

	});

	$(".artist .image").hover(function(){

		$(this).find(\'i\').show();
		$(this).find(\'dl\').show();

		$(this).find(\'dl\').hover(function(){
			$(this).find(\'dd\').show();
		},function(){
			$(this).find(\'dd\').hide();
		});

	},function(){

		$(this).find(\'i\').hide();
		$(this).find(\'dl\').hide();

	});


});
function search_focus(condition){
	switch(condition) {
		case \'click\':if($(\'#search_text\').val()==$(\'#search_text\').attr(\'title\')){
						$(\'#search_text\').val(\'\');
						$(\'#search_text\').removeClass(\'grey\');
						$("#musicsearch").addClass("hasword");
					 }else {
						$(\'#search_text\').removeClass(\'grey\');
						$("#musicsearch").addClass("hasword");
					 }
					 break;
		case \'blur\':if($(\'#search_text\').val()==""){
						$(\'#search_text\').val($(\'#search_text\').attr(\'title\'));
						$("#musicsearch").removeClass("hasword");
						$(\'#search_text\').addClass("grey");
					}
					break;
		default:if($(\'#search_text\').val()==$(\'#search_text\').attr(\'title\')){
					$(\'#search_text\').val(\'\');
					$(\'#search_text\').removeClass(\'grey\');
					$("#musicsearch").addClass("hasword");
				}
	}
}
</script>


<style>
	.sitemap dl dd a{
		background: none;
		padding: 0;
	}

	.sitemap dl dd{
		padding: 0;
		line-height: 22px;
	}

	.sitemap dl{
		margin: 0;
	}
	.sitemap dl dt{
	font-size: 12px;
	line-height: 22px;
	}
	#footer {zoom:1;}
</style>


<div id="footer" data-spm="1110930425">
	<div class="gap">
	<div class="wrapper">
		<div class="content">
			<div class="sitemap">

				<dl>
					<dt>鍏充簬</dt>
					<dd><a title="鍏充簬鎴戜滑" href="http://www.xiami.com/about">鍏充簬鎴戜滑</a></dd>
					<dd><a title="铏剧背鎷涜仒" href="http://www.xiami.com/job">铏剧背鎷涜仒</a><sup class="hot"></sup></dd>
										<dd><a title="鐙珛闊充箰浜哄悎浣?" href="http://www.xiami.com/musician-contact">鐙珛闊充箰浜哄悎浣?</a></dd>
					<dd><a title="鑱旂郴鎴戜滑" href="http://www.xiami.com/contact">鑱旂郴鎴戜滑</a></dd>
					<dd><a title="鍙嬫儏閾炬帴" href="http://www.xiami.com/links">鍙嬫儏閾炬帴</a></dd>
				</dl>

				<dl>
					<dt>鐗硅壊鏈嶅姟</dt>
					<dd><a title="铏剧背 VIP" href="http://www.xiami.com/vip">铏剧背 VIP</a></dd>
					<dd><a title="闊充箰杈句汉" href="http://www.xiami.com/relation/talentcollect">闊充箰杈句汉</a></dd>
					<dd><a title="铏剧背灏忕粍" href="http://www.xiami.com/group">铏剧背灏忕粍</a></dd>
					<dd><a title="铏剧背 LOOP" href="http://loop.xiami.com/">铏剧背 LOOP</a></dd>
					<dd><a title="铏剧背鎾挱" href="http://www.xiami.com/widget">铏剧背鎾挱</a></dd>
					<dd><a title="闊充箰涓撻" href="http://www.xiami.com/events">闊充箰涓撻</a></dd>

				</dl>

				<dl>
					<dt>铏剧背浜戦煶涔?</dt>
					<dd><a title="铏剧背 for iPhone" href="http://www.xiami.com/apps/iphone">铏剧背 for iPhone</a><sup class="hot"></sup></dd>
					<dd><a title="铏剧背 for Android" href="http://www.xiami.com/apps/android">铏剧背 for Android</a></dd>
					<dd><a title="铏剧背 for Windows" href="http://www.xiami.com/apps/win">铏剧背 for Windows</a></dd>
					<dd><a title="铏剧背 for Mac" href="http://www.xiami.com/apps/mac">铏剧背 for Mac</a></dd>
					<dd><a title="铏剧背 for iPad" href="http://www.xiami.com/apps/ipad">铏剧背 for iPad</a></dd>
				</dl>


				<dl>
					<dt>鏇村</dt>
					<dd><a title="鍒嗙被鎵炬瓕" href="http://www.xiami.com/music/category">鍒嗙被鎵炬瓕</a></dd>
					<dd><a title="甯姪涓績" href="http://www.xiami.com/websitehelp">甯姪涓績</a></dd>
					<dd><a title="娣诲姞铏剧背杩樻病鏈夌殑璧勬枡" href="http://www.xiami.com/wiki/addalbum">娣诲姞铏剧背杩樻病鏈夌殑璧勬枡</a></dd>
					<dd><a title="鎻愪氦澶у鎯宠鐨勪笓杈?" href="http://www.xiami.com/music/want">鎻愪氦澶у鎯宠鐨勪笓杈?</a></dd>
					<dd><a title="缁欒櫨绫虫彁鎰忚" href="http://www.xiami.com/group/join/id/10147/_xiamitoken/facce59c1eb871debb79f44385b78f43?done=/group/thread-new/id/10147">缁欒櫨绫虫彁鎰忚</a></dd>
					<dd><a title="铏句紶" href="http://www.xiami.com/software/allegro">铏句紶</a></dd>
				</dl>
			</div>

			<div class="cooperation">
							</div>

		</div>
		<div class="ali_group">
	<a href="http://page.1688.com/shtml/about/ali_group1.shtml" target="_black">闃块噷宸村反闆嗗洟</a>
	<a href="http://www.alibaba.com" target="_black">闃块噷宸村反鍥介檯绔?</a>
	<a href="http://www.1688.com" target="_black">闃块噷宸村反涓浗绔?</a>
	<a href="http://www.aliexpress.com" target="_black">鍏ㄧ悆閫熷崠閫?</a>
	<a href="http://www.taobao.com" target="_black">娣樺疂缃?</a>
	<a href="http://www.tmall.com" target="_black">澶╃尗</a>
	<a href="http://ju.taobao.com" target="_black">鑱氬垝绠?</a>
	<a href="http://www.etao.com" target="_black">涓?娣?</a>
	<a href="http://www.alimama.com" target="_black">闃块噷濡堝</a>
	<a href="http://www.alitrip.com" target="_black">闃块噷鏃呰路鍘诲晩</a>
	<a href="http://www.aliyun.com" target="_black">闃块噷浜戣绠?</a>
	<a href="http://www.yunos.com" target="_black">YunOS</a>
	<a href="http://aliqin.tmall.com" target="_black">闃块噷閫氫俊</a>
	<a href="http://www.laiwang.com/" target="_black">鏉ュ線</a>
	<a href="http://www.alipay.com" target="_black">鏀粯瀹?</a>
	<a href="http://www.net.cn" target="_black">涓囩綉</a>
	<a href="http://www.autonavi.com/" target="_black">楂樺痉</a>
	<a href="http://www.uc.cn/" target="_black">浼樿</a>
	<a href="http://www.umeng.com/" target="_black">鍙嬬洘</a>
	<a href="http://kanbox.com/" target="_black">閰风洏</a>
	<a href="http://www.xiami.com" target="_black">铏剧背</a>
	<a href="http://www.ttpod.com/" target="_black">澶╁ぉ鍔ㄥ惉</a>
	<a href="http://www.dingtalk.com/?lwfrom=20150205111444391" target="_black">閽夐拤</a>
		<div class="extra">
			<div class="sns">
				鍏虫敞铏剧背锛?
				<a href="http://t.sina.com.cn/xiamixiamixiami" title="鏂版氮寰崥"><b class="icon sina"></b></a>
				<a href="http://page.renren.com/699099957/index" title="浜轰汉缃?"><b class="icon renren"></b></a>
				<a href="http://new.qzone.qq.com/810167634" title="QQ 绌洪棿"><b class="icon qzone"></b></a>
				<a href="http://t.qq.com/xiaxiaomi" title="鑵捐寰崥"><b class="icon tqq"></b></a>
								<a href="http://www.douban.com/people/xiaxiaomi" title="璞嗙摚"><b class="icon douban"></b></a>
							</div>

			<div class="copyright">&copy; 2007 - <script>document.write(new Date().getFullYear());</script> <a href="http://www.xiami.com/">闃块噷宸村反(鏉窞)鏂囧寲鍒涙剰鏈夐檺鍏徃</a> - <a href="http://www.xiami.com/sitemap" title="缃戠珯鍦板浘">缃戠珯鍦板浘</a> <strong class="xiami_motto ti" title="give music a chance">"give music a chance"</strong><br /><a href="http://img.xiami.net/res/v3/img/wenwangwen.jpg" target="_blank">娴欑綉鏂嘯2011]0012-005鍙?</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.miibeian.gov.cn/" target="_blank" title="娴橧CP澶?08103200鍙?-2">娴橧CP澶?08103200鍙?-2</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://img.xiami.net/res/v3/img/icp.jpg" target="_blank">缁忚惀璁稿彲璇佺紪鍙? 娴橞2-20110188</a>&nbsp;&nbsp;&nbsp;&nbsp;闃块噷宸村反鏃椾笅缃戠珯</div>
		</div>
	</div>
	</div>
</div>
<!-- #footer-->

<a id="gotop" href="javascript:void(0);" class="t_hide">Top</a>

<div id="personal_hover" style="display:none;"></div>
<textarea id="personal_hover_tpl" style="display:none;">
	<div id="personal_hover_shadow" class="lightShadow"></div>
	<div id="personal_hover_inner">
	<a id="personal_hover_link" href="http://www.xiami.com/u/%uid%" title=" %gmt_access% "><img id="personal_hover_img" src="%avatar%" width="50" height="50" /></a>
	<img class="hidden" id="personal_hover_pulser_img" src="http://img.xiami.net/res/img/default/loading50x50.gif" width="50" height="50" alt="" />
	<div id="personal_trigger_bar">
	<a class="personal_drop" id="personal_menu_down" href="javascript:;" title="">鏇村鍐呭</a>
	<div id="personal_menu_show" class="personal_buddy_menus" style="display:none;">
	<span class="blank_block"></span>
	<p id="personal_relationship_g"><span class="be_contacts"><strong>%nick_name%</strong></span></p>
	<div id="personal_menu_other_div">
		<a id="personal_o_index" class="blocks" href="http://www.xiami.com/u/%uid%" title="%nick_name%鐨勪釜浜轰富椤?">%nick_name%鐨勪釜浜轰富椤?</a>
<!--		<a id="personal_o_minifeed"  class="blocks" href="http://www.xiami.com/space/feed/u/%uid%" title="杩戝喌">杩戝喌</a>-->
		<a id="personal_o_library"  class="blocks" href="http://www.xiami.com/space/lib-song/u/%uid%" title="%nick_name%鐨勯煶涔愬簱">闊充箰搴?</a>
        <a id="personal_o_recommend"  class="blocks" href="http://www.xiami.com/space/rec/u/%uid%" title="%nick_name%鐨勫垎浜?">鍒嗕韩</a>
        <a id="personal_o_contact"  class="blocks" href="http://www.xiami.com/space/following/u/%uid%" title="%nick_name%鐨勫叧娉ㄥ拰绮変笣">鍏虫敞/绮変笣</a>
		<a id="personal_o_collect"  class="blocks" href="http://www.xiami.com/space/collect/u/%uid%" title="%nick_name%鐨勭簿閫夐泦">绮鹃?夐泦</a>
<!--		<a id="personal_o_charts"  class="blocks" href="http://www.xiami.com/space/charts/u/%uid%" title="涓汉鎺掕姒?">涓汉鎺掕姒?</a>-->
		<a id="personal_o_topic"  class="blocks" href="http://www.xiami.com/space/group-thread/u/%uid%" title="%nick_name%鍙備笌杩囩殑璇濋">鍙備笌鐨勮瘽棰?</a>
	</div>
	<a id="personal_msgsned" class="blocks_out" href="http://www.xiami.com/member/sendpm?to_user_id=%uid%" title="鍙戠珯鍐呬俊">鍙戠珯鍐呬俊</a>
	<a id="personal_block_usr" class="blocks_out" href="javascript:;" onclick="blacklist(\'%uid%\');return false;" title="鍔犲叆榛戝悕鍗?">鍔犲叆榛戝悕鍗?</a>
	<div id="person_menu_self_div"></div>
	</div>
	</div>
	</div>
</textarea>



<script>
;(function($){
	$.fn.personalDropMenu = function(settings){
		var defaults = {
			menuDiv: \'#personal_hover\',
			tplDiv: \'#personal_hover_tpl\',
			dropdownArrow:\'#personal_menu_down\',
			myUid: 0
		};

		$.extend(defaults, settings);

		var $menuDiv,menuDiv_html,$tplDiv;
		$menuDiv = $(defaults.menuDiv);
		$tplDiv = $(defaults.tplDiv);
		menuDiv_html = $tplDiv.val();//淇濆瓨鍘熷鐨刪tml
		$menuDiv.bind(\'mouseleave\',function(){$(this).hide();});
		window.isFriendshipQueryed=false;
		var friends;
		var setFriendHtml = function(uid,$obj){
			$obj.next().remove();
			if(uid == defaults.myUid) {
				$obj.html(\'<strong>浣犺嚜宸?</strong>\');
				$menuDiv.find(\'#personal_block_usr\').remove();
				$menuDiv.find(\'#personal_msgsned\').remove();
			}else if(!friends){
				$obj.after(\'<span class="be_stranger"><a href="javascript:;" onclick="attention(\'+uid+\',1);">(鍔犲叧娉?)</a></span>\');
			}else if(friends[\'f_\'+uid] && friends[\'f_\'+uid]=="1"){
				$obj.after(\'<span class="be_stranger"> 宸插叧娉? <a href="http://www.xiami.com/member/attention/uid/\'+uid+\'/type/2?_xiamitoken=\'+_xiamitoken+\'" onclick="return confirm(\\'纭畾瑕佸彇娑堝悧锛焅\');">(鍙栨秷鍏虫敞)</a></span>\');
			}else if(friends[\'f_\'+uid] && friends[\'f_\'+uid]=="2"){
				$obj.after(\'<span class="be_stranger"> 宸插叧娉? <a href="http://www.xiami.com/member/attention/uid/\'+uid+\'/type/2?_xiamitoken=\'+_xiamitoken+\'" onclick="return confirm(\\'纭畾瑕佸彇娑堝悧锛焅\');">(鍙栨秷鍏虫敞)</a></span>\');
			}else if(friends[\'f_\'+uid] && friends[\'f_\'+uid]=="3"){
				$obj.after(\'<span class="be_stranger"> 宸插姞鍏ラ粦鍚嶅崟 <a href="http://www.xiami.com/member/attention/uid/\'+uid+\'/type/2?_xiamitoken=\'+_xiamitoken+\'" onclick="return confirm(\\'纭畾瑕佸彇娑堝悧锛焅\');">(鍙栨秷)</a></span>\');
				$menuDiv.find(\'#personal_block_usr\').remove();
				$menuDiv.find(\'#personal_msgsned\').remove();
			}else{
				$obj.after(\'<span class="be_stranger"><a href="javascript:;" onclick="attention(\'+uid+\',1);">(鍔犲叧娉?)</a></span>\');
			}
		};

		return this.each(function(){
			var $this;
			$this = $(this);
			$this.mouseover(function(){
				var params ={
					uid: /\d+/.exec($this.attr(\'href\')),
					avatar: $this.find(\'img\').attr(\'src\'),
					nick_name:$this.attr(\'title\'),
					gmt_access:$this.attr(\'rel\')
				};
				if(params.gmt_access!=\'\') params.gmt_access = "鏉ヨ鏃堕棿: "+params.gmt_access;
				var html = menuDiv_html.parseTpl(params);
				//var rects = $this[0].getBoundingClientRect();
				var rects = $this.offset();
				var bodyRects = $(\'body\')[0].getBoundingClientRect();
				//var left = rects.left - bodyRects.left - 6;
				//var top = rects.top - bodyRects.top - 6;
				var left = rects.left - 6;
				var top = rects.top - 6;
				$menuDiv.css({\'top\':top,\'left\':left});
				$menuDiv.html(html).show();
				if(params.gmt_access==\'\') $menuDiv.find(\'#personal_hover_link\').attr(\'title\',\'\');
				$menuDiv.find(defaults.dropdownArrow).click(function(){
					var $this = $(this);
					var $next = $this.next();
					$this.toggleClass(\'active\')
					$next.toggle();
					if($next.css(\'display\')!=\'block\') return;
					$relation = $next.find(\'.be_contacts\');
					if(params.uid ==defaults.myUid) {setFriendHtml(params.uid,$relation); return; }
					if(isFriendshipQueryed){ setFriendHtml(params.uid,$relation); return; }
					if(!myUid) return;
					$relation.after($loading2);
					$.getJSON(\'/member/get-friends/_xiamitoken/\'+_xiamitoken,function(data){
						try{
							$relation.next().remove();
							if(data.status == \'failed\'){return false;}
							isFriendshipQueryed = true;
							friends = data.friends;
							setFriendHtml(params.uid,$relation);
						}catch(e){alert(\'Warning:something wrong! Please retry!\');return;}
					});
				});
			});
		});
	};
})(jQuery);


// var myUid = parseInt(\'\');
// $(\'.personalDropDown\').personalDropMenu({myUid:myUid});
</script>

<script>
_xiamitoken = \'facce59c1eb871debb79f44385b78f43\';


$(document).ready(function(){
	$(\'body\').click(function(e){
		$(".ctrl_gears_more").addClass(\'hidden\');
		$(".bt_cdgears").removeClass(\'active\');
	});

	$("#web_loading").remove();

	$(".song_menu").mouseover(function() {
		$(this).css(\'z-index\',\'6\').children(\'span\').show();
	}).mouseout(function() {
		$(this).css(\'z-index\',\'5\').children(\'span\').hide();
	});

	$(".bt_cdgears").mouseover(function(){$(this).addClass(\'active\').next().removeClass(\'hidden\').show();});
	BackTop(\'gotop\');

	// if ($.cookie(\'fools_day\') != 1) {
	// 	var now = new Date();
	// 	var close_date = new Date(\'2012/4/2\');
	// 	var begin_date = new Date(\'2012/4/1\');
	// 	if (close_date.getTime()-now.getTime()>0 && now.getTime()-begin_date.getTime()>0) {
	// 		var rabbit_hole = Math.ceil(Math.random()*4);
	// 		if (rabbit_hole != 3) {
	// 			setTimeout(function() {
	// 				$.cookie(\'fools_day\', 1 , { expires: 3, path: \'/\', domain: \'.xiami.com\'});
	// 				location.href = \'/event/heavenconcert\';
	// 			}, 3000);
	// 		}
	// 	}
	// }
});
var BackTop=function(btnId){
	var btn=document.getElementById(btnId);
	var browserName=navigator.userAgent.toLowerCase();
	if(/chrome/i.test(browserName) && /webkit/i.test(browserName) && /mozilla/i.test(browserName)){
	    var d = document.body;
	}else if(/webkit/i.test(browserName) && !this.chrome){
		var d = document.body;
	}else{
	    var d = document.documentElement ? document.documentElement : document.body;
	}
	/*var d = document.documentElement ? document.documentElement : document.body;*/
	window.onscroll=set;
	btn.onclick=function (){
		btn.className = \'t_hide\';
		window.onscroll=null;
		this.timer=setInterval(function(){
			//d.scrollTop = 0;
			d.scrollTop-=Math.ceil(d.scrollTop*0.8);
			if(d.scrollTop==0) clearInterval(btn.timer,window.onscroll=set);
		},10);
	};
	function set(){
		btn.className = d.scrollTop >= 1200 ? \'t_show\' : \'t_hide\';
	}
};
var checkFlash=function(a){var b=\'妫?娴嬪埌鎮ㄧ郴缁烣lash鎻掍欢鐗堟湰杩囦綆,涓轰簡鏇村ソ鐨勪娇鐢ㄨ櫨绫抽煶涔?,璇峰崌绾ф偍鐨凢lash鎻掍欢, <a href="http://get.adobe.com/cn/flashplayer/" target="_blank" style="color:#36c">椹笂鍗囩骇</a>\',c=function(){var a,c,b=document.body.children||document.body.childNodes;for(c=0;c<b.length;c++)if(1==b[c].nodeType){a=b[c];break}return a}(),d=function(){var c,a=navigator,b=0;if(a.plugins&&a.mimeTypes.length)c=navigator.plugins["Shockwave Flash"],c&&(b=c.description.replace(/.*\s(\d+\.\d+).*/,"$1"));else try{c=new window.ActiveXObject("ShockwaveFlash.ShockwaveFlash"),c&&(b=c.GetVariable("$version"))}catch(d){}return b}(),e=function(){var a=document.createElement("div");a.innerHTML=b,a.style.backgroundColor="#FFF9D7",a.style.borderBottom="1px solid #E3C823",a.style.fontWeight="bold",a.style.lineHeight="30px",a.style.textAlign="center",a.style.color="#f60",document.body.insertBefore(a,c)},f=d?d.match(/\d+/g):-1,g=f.length>0?f.join("."):0;return!g||parseInt(f[0],10)<a?(e(),!1):!0}(9);
</script>




<div id="cnzz" style="display:none">
<script type="text/javascript">
(function (d) {
var z1=d.createElement("script");z1.type="text/javascript";z1.async=true;
var z2=d.createElement("script");z2.type="text/javascript";z2.async=true;
z1.src=("https:"==d.location.protocol?"https://":"http://")+"s95.cnzz.com/stat.php?id=921634&web_id=921634";
z2.src=("https:"==d.location.protocol?"https://":"http://")+"s16.cnzz.com/stat.php?id=2629111&web_id=2629111";
d.getElementById("cnzz").appendChild(z1);
d.getElementById("cnzz").appendChild(z2);
})(document);
</script>
<!-- <script src=\'http://s95.cnzz.com/stat.php?id=921634&web_id=921634\' language=\'JavaScript\' charset=\'gb2312\'></script> -->
<!-- <script src="http://s16.cnzz.com/stat.php?id=2629111&web_id=2629111" language="JavaScript"></script> -->
</div>



<div id="dfp" style="display:none">
<script>
(function() {
var gads = document.createElement(\'script\');
gads.async = true;
gads.type = \'text/javascript\';
var useSSL = \'https:\' == document.location.protocol;
gads.src = (useSSL ? \'https:\' : \'http:\') +
\'//www.googletagservices.com/tag/js/gpt.js\';
//var node = document.getElementsByTagName(\'script\')[0];
//node.parentNode.insertBefore(gads, node);
document.getElementById("dfp").appendChild(gads);
})();
</script>
</div>


<div style="background:#fff; margin: 0 auto;display:none;"><font style="font-size:12px; color:#fff;">Host: , Process All 0.0664s Memory:3575.38k <br></font></div>
</body>
</html>
'''
result = re.findall(p, myStr)

print result
