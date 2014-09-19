$(document).ready(function() {
    $("input[type=file]").change(function() {
        $("form").submit();
    });
    
    $('.upload').click(function() {
        $("input[type=file]").click();
    });
});
                  
