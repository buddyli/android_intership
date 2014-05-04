<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8" />
<title>类型列表</title>
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
		<h1>类型列表</h1>
		<form name="frm_list_item" id="frm_list_item" action="" method="post">
		<div class="box">
			<table>
				<tr>
					<th width="40%">名称</th>
					<th width="30%">录入时间</th>
					<th width="10%">关联条目</th>
					<th width="20%" colspan="2">操作</th>
				</tr>
				% for item in data:
				<tr>
					<td>${item.name}</td>
					<td>${item.addTimeStr}</td>
					<td><a href="/to_add_type_item?id=${item.id}">关联条目</a></td>
					<td><a href="/to_modify_type?id=${item.id}">修改</a></td>
					<td><a href="/del_type?id=${item.id}">删除</a></td>
				</tr>
				% endfor
			</table>
		</div>
		</from>
	</div>
</body>
</html>
