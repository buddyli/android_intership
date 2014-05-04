<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8" />
<title>首页</title>
<meta name="format-detection" content="telephone=no" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-touch-fullscreen" content="yes">
<meta name="viewport"
	content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no" />
<link rel="stylesheet" media="screen" type="text/css"
	href="/static/css/active.css" />
</head>
<body>
	<div class="box">
		<h1>首页</h1>
		<table>
			<tr>
				<td><a href="${site_opt['static_url']}/static/item_add.html">添加条目</a></td>
			</tr>
			<tr>
				<td><a href="/list_item?start=0&size=1000">条目列表</a></td>
			</tr>
			
			<tr>
				<td><a href="/static/type_add.html">添加类型</a></td>
			</tr>
			<tr>
				<td><a href="/list_type?start=0&size=1000">类型列表</a></td>
			</tr>

			<tr>
				<td><a href="/to_add_content">添加内容</a></td>
			</tr>
			<tr>
				<td><a href="/list_content?start=0&size=1000">内容列表</a></td>
			</tr>
		</table>
	</div>
</body>
</html>
