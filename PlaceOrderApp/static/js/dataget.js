$(".sub").click( function() {
 $.post( $("#myForm").attr("action"),
         $("#myForm :").serializeArray(),
         function(info){ $("#result").html(info);
   });
clearInput();
});

$("#myForm").submit( function() {
  return false;
});
function clearInput() {
    $("#myForm :input").each( function() {
       $(this).val('');
    });
}