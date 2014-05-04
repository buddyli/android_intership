<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8" />
<title>内容列表</title>
<meta name="format-detection" content="telephone=no" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-touch-fullscreen" content="yes">
<meta name="viewport"
	content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no" />
<link rel="stylesheet" media="screen" type="text/css"
	href="/static/css/active.css" />
<script type="text/javascript" src="/static/js/jquery-1.8.3.min.js"></script>
</head>
<body>
	<div class="box">
		<h1>内容列表</h1>
		<form name="frm_list_content" id="frm_list_content" action="" method="post">
		<div class="box">
			<table>
				<tr>
					<th width="20%">名称</th>
					<th width="10%">索引</th>
					<th width="10%">录入时间</th>
					<th width="40%">ITEM值</th>
					<th width="20%" colspan="2">操作</th>
				</tr>
				% for item in data:
				<tr>
					<td>${item.name}</td>
					<td>
						% if item.indexed == '0':
						已索引
						% else:
						未索引
						% endif
					</td>
					<td>${item.addTimeStr}</td>
					<td>${item.itemValue}</td>
					<td><a href="/to_modify_content?id=${item.id}">修改</a></td>
					<td><a href="/del_content?id=${item.id}">删除</a></td>
				</tr>
				% endfor
			</table>
		</div>
		</from>
	</div>
</body>
</html>
