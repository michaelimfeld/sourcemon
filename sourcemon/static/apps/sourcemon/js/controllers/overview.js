(function(module) {
    var OverviewController = function(servers) {
        var self = this;
        self.servers = servers;
    };

    module.controller('OverviewController', OverviewController);
}(angular.module('sourcemon')));
