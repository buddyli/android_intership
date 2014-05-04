<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8" />
<title>关联条目</title>
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
		<h1>关联条目</h1>
		<form name="frm_modify_type" id="frm_modify_type" action="/add_type_item" method="POST">
			<table>
				<tr>
					<td>
						名称：<input name="name" id="name" value="{{data.name}}">
						<input type="hidden" name="id" value="{{data.id}}">
					</td>
				</tr>
				<tr>
					<td>
						条目：
						% for item in items:
						% 	flag = False
						% 	for p in data.items:
						%		if p.id == item.id:
						%			flag = True
						%			break;
						%		end
						%	end

						%	if flag:
						<input type="checkbox" name="items" id="items_{{item.id}}" value="{{item.id}}" checked="checked">{{item.name}}&nbsp;&nbsp;
						%	else:
						<input type="checkbox" name="items" id="items_{{item.id}}" value="{{item.id}}">{{item.name}}&nbsp;&nbsp;
						%	end
						% end
					</td>
				</tr>
				<tr>
					<td>
						<input type="submit" value="提交">
					</td>
				</tr>
			</table>
		</from>
	</div>
</body>
</html>
