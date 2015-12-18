(function() {
    var module = angular.module('sourcemon', ['ng', 'ngRoute']);

    module.config(function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '/static/apps/sourcemon/templates/overview.html',
                controller: 'OverviewController',
                controllerAs: 'overview',
                resolve: {
                    servers: function(dataService) {
                        servers = dataService.getServers();
                        servers.then(servers)
                        {
                            return servers;
                        }
                    }
                }
            })
            .otherwise({redirectTo: '/'});
    });
}());
