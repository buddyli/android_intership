<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>订单列表</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th>手机号码</th>
                    <th>菜单</th>
                    <th>餐馆</th>
                    <th>录入时间</th>
                    <th colspan='3'>操作</th>
                </tr>
            </thead>
                
            <tbody>
                %if data and 'types' in data:
                    % for item in data['types']:
                    <tr>
                        <td>${item['mobile'] if 'name' in item else '--'}</td>
                        <td>${item['ordered'] if 'ordered' in item else '--'}</td>
                        <td>
                            % if item.restaurant != None:
                            ${item['restaurant']['name']}
                            % else:
                            '--'
                            % endif
                        </td>
                        <td>${item['addTimeStr'] if 'addTimeStr' in item else '--'}</td>
                        <td>
                            <a class="edit" href="/modify_order?id=${item.id}&status=1">接受</a>
                        </td>
                        <td>
                            <a class="edit" href="/modify_order?id=${item.id}&status=3">等待</a>
                        </td>
                        <td>
                            <a class="delete" href="/modify_order?id=${item.id}&status=2" onclick="javascript:return confirm('Yes or No?')">拒绝</a>
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