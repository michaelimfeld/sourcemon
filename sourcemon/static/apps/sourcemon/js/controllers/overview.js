(function(module) {
    var OverviewController = function(servers, dataService) {
        var self = this;
        self.servers = servers;

        self.getServers = function(){
            servers = dataService.getServers();
            servers.then(function(servers){
                self.servers = servers;
            });
        };
    };

    module.controller('OverviewController', OverviewController);
}(angular.module('sourcemon')));
