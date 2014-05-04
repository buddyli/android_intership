<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/modify_type"><!-- Form -->
            <fieldset><legend>编辑类型</legend>
                <%
                    item = data['item'] if data and 'item' in data else None
                %>

                <div class="input_field">
                    <label for="b">名称</label>
                    <input class="mediumfield" name="name" type="text" value="${ item['name'] if 'name' in item else ''}" />
                </div>

                <input name="id" type="hidden" value="${ item['id'] if 'id' in item else ''}" />
                        
                <input class="submit" type="submit" value="提交" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>