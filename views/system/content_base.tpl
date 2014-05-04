<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title><%block name="title">Website Name | Splash Manager</%block></title>

<%block name="global_css">
    <!-- Loading CSS file -->
    <style type="text/css" media="all">
    /* Load framework elements */
    @import url(${site_opt['static_url']}/static/m/css/framework.css);
    /* Now, lets set the style */
    @import url(${site_opt['static_url']}/static/m/styles/style_coffee.css);
    </style>
</%block>

    <style type="text/css">
        img { behavior: url(${site_opt['static_url']}/static/m/js/iepngfix.htc) !important; }
        .navbullet { behavior: url(${site_opt['static_url']}/static/m/js/iepngfix.htc) !important; }
    </style> 

<%block name="global_js">
    <!-- Loading javascript -->
    <script src="${site_opt['static_url']}/static/m/js/jquery.js" type="text/javascript"></script>
    <script src="${site_opt['static_url']}/static/m/js/functions.js" type="text/javascript"></script>
</%block>

<%block name="local_js">
    <!-- Loading local javascript-->
    <script type="text/javascript" src="${site_opt['static_url']}/static/m/js/json2.js"></script>
    <script type="text/javascript">
    function changeItem(id){
        $.post('selectItems', {'typeId': id}, function(json){
            $('#cascade_items').html('');
            for(var i=0; i<json.length; i++){
                var p = "<div><label for='a' id='"+json[i][3]+"' name='"+json[i][0]+"' innerName='"+json[i][2]+"'>"+json[i][0]+"</label><input class='mediumfield' type='text' name='item_"+json[i][0]+" id='item_"+json[i][0]+"'/>";
                if (json[i][1] == '1')
                     p += "索引:<input type='checkbox' name='item_indexed_'"+json[i][0]+"' id='item_indexed_'"+json[i][0]+"/>";
                else
                    p += "索引:<input type='checkbox' name='item_indexed_'"+json[i][0]+"' id='item_indexed_'"+json[i][0]+" checked='checked'/>";
                p += "</p></div>";
                $('#cascade_items').append(p);
            }
        }, 'json');
    }

    function Item(attrName, attrValue, indexed){
        this.attrName = attrName;
        this.attrValue = attrValue;
        this.indexed = indexed;
    }

    // 字符串转换成json数据
    function strToJson(str){
        return eval('(' + str + ')')
    }

    $(function(){
        $("#types").change(function(){
            typeId = $(this).val();
            if (typeId == -1){

            }else{
                changeItem(typeId);
            }
        });

        $('#frm_add_content').submit(function(){
            var val = '[';
            var tmp = $("div#cascade_items div");
            var array = new Array();

            for(var i=0; i<tmp.length; i++){
                var input = $("input[name^='item_']", tmp[i]).val();
                var id = $("label", tmp[i]).attr('id');
                var name = $("label", tmp[i]).attr('name');
                var innerName = $("label", tmp[i]).attr('innerName');
                var indexed = $("input[name^='item_indexed_']", tmp[i]).attr('checked');

                var indexedStr = '0';
                if (!indexed){//没有选中时，再将状态置为未选中
                    indexedStr = '1';
                }

                var obj = strToJson('{\''+id+'\':\''+input+'\',indexed:\''+indexedStr+'\'}');
                array[i] = obj;
            }
            $("#itemValues").val(JSON.stringify(array));
        })
    })
    </script>

</%block>

</head>
<body>

<div id="container"> <!-- Container begins here -->  
    <div id="sidebar"> <!-- Sidebar begins here -->

    <%block name="siderbar">
        <div class="header logo"> <!-- Logo begins here -->
            <a href="javascript:;" title=""><img src="${site_opt['static_url']}/static/m/images/logo.png" alt="" /></a>
        </div> <!-- END Logo -->
                
        <div id="navigation"> <!-- Navigation begins here -->
            <div class="sidenav"><!-- Sidenav -->
                <%include file="inc/sidenav.tpl" />
            </div><!-- /Sidenav -->
        </div> <!-- END Navigation -->
        <div id="copyrights">
            <p><a href="javascript:;" title="">Splash Manager Theme<br />designed by Mastergreed</a>. Live Preview hosted on 
            <a href="javascript:;">WHB</a>.</p>
        </div>
    </%block>

    </div> <!-- END Sidebar -->
    <div id="primary"> <!-- Primary begins here -->

<%block name="content">        
    <div id="content"> <!-- Content begins here -->        
        <div class="box"> <!-- Box begins here -->
            <pre>
                Defualt content html.
            </pre>
        </div>
    <div>
</%block>

    </div> <!-- END Primary --> 
    <div class="clear"></div>
</div> <!-- END Container -->
</body>
</html>