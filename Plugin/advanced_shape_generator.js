(function () {
    var button;

    Plugin.register('advanced_shape_generator', {
        title: 'Advanced shape generator',
        author: 'ultimatech',
        description: 'Allows the creation of more advanced shapes',
        icon: 'pages',
        version: '0.0.2',
        //min_version: '4.0.0',
        variant: 'both',
        onload() {
            AdvancedShapeGeneratorAction = new Action("generate_advanced_shape", {
                name: "Generate Advanced Shape",
                description: "Generates various complex shapes.",
                icon: "pages",
                click: function () {

                    //Check if the user is in the right mode
                    if (!Format.rotate_cubes) {
                        Blockbench.showMessageBox({
                            title: 'Incompatible Format',
                            message: 'This plugin only works in formats that support cube rotations.'
                        })
                        return;
                    }
                    else {
                        shapeWindow();
                    }
                }
            })
            MenuBar.addAction(AdvancedShapeGeneratorAction, "filter");
        },
        onunload() {
            AdvancedShapeGeneratorAction.delete();
        }
    });

    function shapeWindow() {

        var shape_list = {
            sphere: "Sphere",
            pyramid: "Pyramid",
            text: "Text"
        };
        var variable_list = {
            diameter: "Diameter/Length",
            radius: "Radius"

        };

        var shape_window = new Dialog({
            title: 'Shape selector',
            id: 'shape_selector',

            form: {
                shape: { label: "Select shape", type: "select", options: shape_list },
                variable: { label: "Variable", type: "select", options: variable_list },
                value: { label: "Value", type: "number", value: 0 },
                thickness: { label: "Height/Depth", type: "number", value: 8 },
                center: { label: "Center Point", type: "vector", value: [8, 8, 8] },
            },
            lines: [
                '<p><span style="float:left;">Reset values: <button title="Reset values" =button id="reset_shape"><i class="material-icons" style="color:white">refresh</i></button></span></p><br/><br/>'
            ],

            draggable: true,

            onConfirm(result) {
                generateShape(result);
                shape_window.hide();
            }
        });

        shape_window.show();

        if (localStorage.getItem("shape") != undefined) {
            document.getElementById("shape").selectedIndex = localStorage.getItem("shape");
            document.getElementById("variable").selectedIndex = localStorage.getItem("variable");
            $('.dialog#shape_selector input#value').val(localStorage.getItem("value"));
            $('.dialog#shape_selector input#thickness').val(localStorage.getItem("thickness"));
            $('.dialog#shape_selector input#center_0').val(localStorage.getItem("center_x"));
            $('.dialog#shape_selector input#center_1').val(localStorage.getItem("center_y"));
            $('.dialog#shape_selector input#center_2').val(localStorage.getItem("center_z"));
        }

        //Reset Button Click Event
        document.getElementById("reset_shape").onclick = function () {
            document.getElementById("shape").selectedIndex = 0;
            document.getElementById("variable").selectedIndex = 0;
            $('.dialog#shape_selector input#value').val(16);
            $('.dialog#shape_selector input#thickness').val(1);
            $('.dialog#shape_selector input#center_0').val(7.5);
            $('.dialog#shape_selector input#center_1').val(7.5);
            $('.dialog#shape_selector input#center_2').val(7.5);

            localStorage.removeItem("shape");
            localStorage.removeItem("variable");
            localStorage.removeItem("value");
            localStorage.removeItem("thickness");
            localStorage.removeItem("center");
        }
    }










    
})()

onUninstall = function () {
    //Removing entries on uninstall
    Blockbench.removeMenuEntry('Generate Advanced Shape')
};