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
            return $http.post('/api/server/add', data);
        };

        var removeServer = function(id) {
            return $http.post('/api/server/remove/' + id);
        };

        var getServer = function(id) {
            var deferred = $q.defer();
            var resp = $http.get('/api/server/' + id)
                .then(function(response) {
                    deferred.resolve( response.data );
                });
            return deferred.promise;
        };

        return {
            getServers: getServers,
            getServer: getServer,
            addServer: addServer,
            removeServer: removeServer
        };
    };

    module.factory('dataService', dataService);
}(angular.module('sourcemon')));
