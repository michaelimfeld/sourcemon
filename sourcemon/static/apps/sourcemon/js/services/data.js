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

        return {
            getServers: getServers
        };
    };

    module.factory('dataService', dataService);
}(angular.module('sourcemon')));
