    jQuery(function ($) {
      var fbTemplate = document.getElementById("build-wrap");
      var options = {
        onSave: function (evt, formData) {
          console.log("formbuilder 1 saved");
          toggleEdit(false);
          console.log(formData);
          return false;
          $(".render-wrap").formRender({ formData });
        }
      };
      $(fbTemplate).formBuilder(options);
    });

    /**
     * Toggles the edit mode for the demo
     * @return {Boolean} editMode
     */
    function toggleEdit(editing) {
      document.body.classList.toggle("form-rendered", !editing);
    }

    document.getElementById("edit-form").onclick = function () {
      toggleEdit(true);
    };