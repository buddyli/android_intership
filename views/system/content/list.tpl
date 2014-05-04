<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>条目内容</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th width="10%">名称</th>
                    <th width="10%">索引</th>
                    <th width="15%">录入时间</th>
                    <th width="50%">ITEM值</th>
                    <th width="15%" colspan='2'>操作</th>
                </tr>
            </thead>
                
            <tbody>
                %if data and 'items' in data:
                    % for item in data['items']:
                    <tr>
                        <td>${item['name'] if 'name' in item else '--'}</td>
                        <td>
                            ${u'未索引' if item['indexed'] == '1' else u'已索引'}
                        </td>
                        <td>${item['addTimeStr'] if 'addTimeStr' in item else '--'}</td>
                        <td>${item['itemValue'] if 'itemValue' in item else '--'}</td>
                        <td>
                            <a class="edit" href="/to_modify_content?id=${item.id}">修改</a>
                        </td>
                        <td>
                            <a class="delete" href="/del_content?id=${item.id}" onclick="javascript:return confirm('Yes or No?')">删除</a>
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