<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/add_type_item"><!-- Form -->
            <fieldset><legend>关联条目</legend>
                <%
                    type = data['type'] if data and 'type' in data else None
                    items = data['items'] if data and 'items' in data else None
                    itemIds = data['itemIds'] if data and 'itemIds' in data else None
                %>

                <div class="input_field">
                    <label for="b">名称</label>
                    <input class="mediumfield" name="name" type="text" value="${ type['name'] if 'name' in type else ''}" readonly/>
                </div>
                <div class="input_field">
                <label for="b">条目</label>
                % for item in items:
                % if item.id in itemIds:
                    <input type="checkbox" name="items" id="items_${item.id}" value="${item.id}" checked="checked">${item['name']}&nbsp;&nbsp;
                % else:
                    <input type="checkbox" name="items" id="items_${item.id}" value="${item.id}">${item['name']}&nbsp;&nbsp;
                % endif
                % endfor
                </div>
                <input name="id" type="hidden" value="${ type['id'] if 'id' in type else ''}" />
                        
                <input class="submit" type="submit" value="提交" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>