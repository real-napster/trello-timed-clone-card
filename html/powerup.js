// TrelloPowerUp.settings({
//     'card-buttons': function(t, options) {
//       // Erstellen des Button-Elements
//       var button = document.createElement('button');
//       button.innerHTML = 'Click me';
      
//       // Hinzufügen des Button-Elements zur Seite
//       t.get('card-buttons').appendChild(button);
      
//       // Definieren der Funktion, die ausgeführt wird, wenn der Button geklickt wird
//       button.addEventListener('click', function() {
//         alert('Button clicked');
//       });
//     }
//   });

// TrelloPowerUp.initialize({
//     'settings': function(t, options) {
//         return t.popup({
//         title: 'Einstellungen',
//         url: 'index.html'
//         });
//     }
// });

var t = TrelloPowerUp.iframe();

TrelloPowerUp.initialize({
    'card-buttons': function(t, options){
      return [{
        icon: 'https://cdn.glitch.com/1b42d7fe-bda8-4af8-a6c8-eff0cea9e08a%2Frocket-ship.png?1494946700421',
        text: 'Zeitauswahl',
        callback: function(t){
          return t.popup({
            title: "Zeit auswählen",
            url: 'zeit.html'
          });
        }
      }];
    }
  });

t.render(function(){
    t.sizeTo('#time').done();
});
