(function(module) {
    var OverviewController = function(servers, dataService) {
        var self = this;
        self.servers = servers;

        self.addServer = function(){
            var res = dataService.addServer(self.ip_addr, self.port);
            res.success(function(data, status, headers, config) {
                self.getServers()
            });
            res.error(function(data, status, headers, config) {
                alert( "failure message: " + JSON.stringify({data: data}));
            });
        };

        self.getServers = function(){
            servers = dataService.getServers();
            servers.then(function(servers){
                self.servers = servers;
            });
        };
    };

    module.controller('OverviewController', OverviewController);
}(angular.module('sourcemon')));
