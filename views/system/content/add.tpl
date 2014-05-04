<%inherit file="../content_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/add_content" id="frm_add_content"><!-- Form -->
            <fieldset><legend>添加内容</legend>

                <div class="input_field">
                    <label for="a">名称</label>
                    <input class="mediumfield" name="name" type="text" value="" />
                    <span class="field_desc"> * Required</span>
                    <input type="hidden" name="itemValues" id="itemValues">
                </div>

                <div class="input_field">
                    <label for="b">索引</label>
                    <input type="checkbox" name="indexed" id="indexed" checked='checked'>
                    <span class="field_desc"> Optional</span>
                </div>

                <div class="input_field">
                    <label for="a">类型</label>
                    <select name="types" id="types">
                        <option value="-1">选择类型</option>
                        <% types  = data if data else None %>
                        % for type in types:
                            <option value="${type.id}">${type.name}</option>
                        % endfor
                    </select>
                    <span class="field_desc"> * Required</span>
                </div>
                
                <div class="input_field" id="cascade_items">
                </div>

                <input class="submit" type="submit" value="提交" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>