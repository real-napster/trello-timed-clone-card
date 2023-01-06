TrelloPowerUp.settings({
    'card-buttons': function(t, options) {
      // Erstellen des Button-Elements
      var button = document.createElement('button');
      button.innerHTML = 'Click me';
      
      // Hinzufügen des Button-Elements zur Seite
      t.get('card-buttons').appendChild(button);
      
      // Definieren der Funktion, die ausgeführt wird, wenn der Button geklickt wird
      button.addEventListener('click', function() {
        alert('Button clicked');
      });
    }
  });

TrelloPowerUp.initialize({
    'settings': function(t, options) {
        return t.popup({
        title: 'Einstellungen',
        url: 'index.html'
        });
    }
});