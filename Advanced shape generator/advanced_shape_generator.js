(function() {
    var button;

    Plugin.register('advanced_shape_generator', {
        title: 'Advanced shape generator',
        author: 'ultimatech',
        description: 'Allows the creation of more advanced shapes',
        icon: 'bar_chart',
        version: '0.0.1',
        variant: 'both',
        onload() {
            button = new Action('generate_advanced_shape', {
                name: 'Generate Advanced Shape',
                description: 'Allows the creation of more advanced shapes',
                icon: 'bar_chart',
                click: function() {
                    Undo.initEdit({elements: Cube.selected});
                    Cube.selected.forEach(cube => {
                        cube.to[1] = cube.from[0] + Math.floor(Math.random()*8);
                    });
                    Undo.finishEdit('generate advanced shape');
                }
            });
            MenuBar.addAction(button, 'filter');
        },
        onunload() {
            button.delete();
        }
    });

})();