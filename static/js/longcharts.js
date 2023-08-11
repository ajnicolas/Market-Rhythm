var ctx = document.getElementById('longchart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: [
          {% for item in long_labels %}
            "{{ item }}",
          {% endfor %}
        ],

        datasets: [{
            label: 'Long Trades',
            backgroundColor: 'rgba(169,187,200,0.2)',
            borderColor: 'rgba(169,187,200,1)',
            borderWidth: 1,
            data: [
              {% for item in long_trades %}
                "{{ item }}",
              {% endfor %}
            ]

        }, {

            label: 'Long Pnl',
            backgroundColor: 'rgba(0,180,0,0.2)',
            borderColor: 'rgba(0,180,0,1)',
            borderWidth: 1,
            data: [
              {% for item in long_pnl %}
                "{{ item }}",
              {% endfor %}
            ]
        }]
    },

    // Configuration options go here
    options: {

    }
});

var ctx = document.getElementById('gainChart').getContext('2d');
var chart = new Chart(ctx, {
  // The type of chart we want to create
  type: 'line',

  // The data for our dataset
  data: {
      labels: [
        {% for item in long_labels %}
          "{{ item }}",
        {% endfor %}
      ],

      datasets: [{
          label: 'Long Pnl',
          backgroundColor: '#7c98ab',
          borderColor: '#7c98ab',
          // fill: false,
          data: [
            {% for item in long_pnl %}
              "{{ item }}",
            {% endfor %}
          ]
      }]
  },

  // Configuration options go here
  options: {}
});

var ctx = document.getElementById('winloss').getContext('2d');
var chart = new Chart(ctx, {
  // The type of chart we want to create
  type: 'pie',

  // The data for our dataset
  data: {
      labels: ["Win", "Loss"],

      datasets: [{
          label: 'win/loss',
          backgroundColor: ["#0047ab", "#f97f3e"],
          // borderColor: ["#1a1410", "#1a1410"],
          // fill: false,
          data: [
            {% for item in winloss %}
              "{{ item }}",
            {% endfor %}
          ]
      }]
  },

  // Configuration options go here
  options: {
    title: {
      display: true,
      text: 'Longs Win/Loss'
    }
  }
});