<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>菜单列表</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th>名称</th>
                    <th>价格</th>
                    <th>餐馆</th>
                    <th>录入时间</th>
                    <th colspan='2'>操作</th>
                </tr>
            </thead>
                
            <tbody>
                %if data and 'types' in data:
                    % for item in data['types']:
                    <tr>
                        <td>${item['name'] if 'name' in item else '--'}</td>
                        <td>${item['price'] if 'price' in item else '--'}</td>
                        <td>
                            % if item.restaurant != None:
                            ${item['restaurant']['name']}
                            % else:
                            '--'
                            % endif
                        </td>
                        <td>${item['addTimeStr'] if 'addTimeStr' in item else '--'}</td>
                        <!--<td>
                            <a class="edit" href="/to_add_type_item?id=${item.id}">关联餐馆</a>
                        </td>-->
                        <td>
                            <a class="edit" href="/to_modify_type?id=${item.id}">修改</a>
                        </td>
                        <td>
                            <a class="delete" href="/del_type?id=${item.id}" onclick="javascript:return confirm('Yes or No?')">删除</a>
                        </td>
                    </tr>
                    % endfor
                %endif

            </tbody>
        </table><!-- END Table -->
        <div class="box">
            <!-- Page Navigation -->
            %if 'pagenation' in data:
            <ul class="paginator">
                %for p in data['pagenation']:
                <li class="${ 'current' if p == data['cur_page'] else ''}"><a href="/system/manager/list?page=${ p }${ '&_uniq=%s' % data['_uniq'] if '_uniq' in data else ''}">${ p }</a></li>
                %endfor
            </ul>
            %endif
        <!-- /Page Navigation -->
        </div>
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>