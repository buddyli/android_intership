<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/add_item"><!-- Form -->
            <fieldset><legend>添加餐馆</legend>

                <div class="input_field">
                    <label for="a">名称</label>
                    <input class="mediumfield" type="text" name="name" type="text" value="" />
                    <span class="field_desc"> * Required</span>
                </div>

                <div class="input_field">
                    <label for="b">地址</label>
                    <input class="mediumfield" type="text" name="address" id="address" value=""/>
                    <span class="field_desc"> * Required</span>
                </div>
                
                <div class="input_field">
                    <label for="c">电话</label>
                    <input class="mediumfield" type="text" name="telno" id="telno" value=""/>
                    <span class="field_desc"> Optional</span>
                </div>

                <input class="submit" type="submit" value="提交" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>