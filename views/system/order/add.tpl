<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/add_type"><!-- Form -->
            <fieldset><legend>添加菜单</legend>

                <div class="input_field">
                    <label for="a">名称</label>
                    <input class="mediumfield" name="name" type="text" value="" />
                    <span class="field_desc"> * Required</span>
                </div>
                <div class="input_field">
                    <label for="a">价格</label>
                    <input class="mediumfield" name="price" type="text" value="" />
                    <span class="field_desc"> * Required</span>
                </div>

                <%
                    restaurants = data if data else None
                %>
                <div class="input_field">
                    <label for="a">餐馆</label>
                    <!-- <input class="mediumfield" name="restaurant" type="text" value="" /> -->
                    <select name='restaurant' id='restaurant'>
                        <option value="0">Please select restaurant</option>
                        % if restaurants != None:
                        % for item in restaurants:
                        <option value="${item.id}">${item.name}</option>
                        % endfor
                        % endif
                    </select>
                    <span class="field_desc"> * Required</span>
                </div>

                <input class="submit" type="submit" value="提交" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>