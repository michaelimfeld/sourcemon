(function(module) {
    var ServerController = function(server, dataService) {
        var self = this;
        self.data = server;
        self.players = self.data.players;

        self.getDuration = function(dur){
            return Math.round(dur / 60);
        };
    };

    module.controller('ServerController', ServerController);
}(angular.module('sourcemon')));
