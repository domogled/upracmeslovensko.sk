<div class="content">
			<div class="container top" style="">
    <?php require 'index/banner.php'; ?>



    <?php require 'index/velke_menu_var_1.php'; ?>


            <?php require 'index/velke_menu_var_2.php'; ?>


            <?php require 'index/velke_menu_var_3.php'; ?>




    <script>
        $(function () {
            $(".block td.text-center").mouseover(function() {
                $(this).addClass("pulse");
            });
            $(".block td.text-center").mouseout(function() {
                $(this).removeClass("pulse");
            });

        });
    </script>
    <?php require 'content_content_block.php'; ?>

</div>
		</div>
		
