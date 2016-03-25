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
            .when('/server/:id', {
                templateUrl: '/static/apps/sourcemon/templates/server.html',
                controller: 'ServerController',
                controllerAs: 'server',
                resolve: {
                    server: function(dataService, $route) {
                        server = dataService.getServer($route.current.params.id);
                        server.then(server)
                        {
                            return server;
                        }
                    }
                }
            })
            .when('/addserver', {
                templateUrl: '/static/apps/sourcemon/templates/addserver.html',
                controller: 'AddServerController',
                controllerAs: 'ctrl'
            })
            .otherwise({redirectTo: '/'});
    });
}());
