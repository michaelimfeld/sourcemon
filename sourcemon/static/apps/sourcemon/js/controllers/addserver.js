(function(module) {
    var addServerController = function(dataService, $location) {
        var self = this;

        self.addServer = function(){
            var res = dataService.addServer(self.ip_addr, self.port);
            res.success(function(data, status, headers, config) {
                $location.path('/');
            });
            res.error(function(data, status, headers, config) {
                alert( "failure message: " + JSON.stringify({data: data}));
            });
        };
    };

    module.controller('AddServerController', addServerController);
}(angular.module('sourcemon')));
