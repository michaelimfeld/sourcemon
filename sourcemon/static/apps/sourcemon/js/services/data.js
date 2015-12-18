(function(module) {
    var dataService = function($http, $q) {
        var getServers = function() {
            var deferred = $q.defer();
            var resp = $http.get('/api/servers')
                .then(function(response) {
                    deferred.resolve( response.data );
                });
            return deferred.promise;
        };

        var addServer = function(ip_addr, port) {
            var data = {
                'ip_addr': ip_addr,
                'port': port
            };
            return $http.post('/api/servers', data);
        };

        return {
            getServers: getServers,
            addServer: addServer
        };
    };

    module.factory('dataService', dataService);
}(angular.module('sourcemon')));
