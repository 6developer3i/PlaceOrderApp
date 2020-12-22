jQuery(function($) {
    var fbEditor = document.getElementById('build-wrap');
    var formBuilder = $(fbEditor).formBuilder();
    var buttons = document.getElementsByClassName('addFieldBtn');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].onclick = function() {
        var field = {
            type: 'text',
            class: 'form-control',
            label: this.dataset.label + ' added at: ' + new Date().getTime()
          };
          var index = this.dataset.index ? Number(this.dataset.index) : undefined;
  
        formBuilder.actions.addField(field, index);
      };
    }
  });