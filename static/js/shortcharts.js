var ctx = document.getElementById('shortchart').getContext('2d');
var chart = new Chart(ctx, {
  // The type of chart we want to create
  type: 'line',

  // The data for our dataset
  data: {
      labels: [
        {% for item in short_labels %}
          "{{ item }}",
        {% endfor %}
      ],

      datasets: [{
          label: 'Short Trades',
          backgroundColor: 'rgba(169,187,200,0.2)',
          borderColor: 'rgba(169,187,200,1)',
          borderWidth: 1,
          // fill: false,
          data: [
            {% for item in short_trades %}
              "{{ item }}",
            {% endfor %}
          ]

      }, {

          label: 'Short Pnl',
          backgroundColor: 'rgba(255,99,132,0.2)',
          borderColor: 'rgba(255,99,132,1)',
          borderWidth: 1,
          // fill: false,
          data: [
            {% for item in short_pnl %}
              "{{ item }}",
            {% endfor %}
          ]
      }]
  },

  // Configuration options go here
  options: {}
});