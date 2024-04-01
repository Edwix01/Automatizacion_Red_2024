(function (nx) {
    // Define CustomLinkClass
    nx.define('CustomLinkClass', nx.graphic.Topology.Link, {
        properties: {
            sourcelabel: null,
            targetlabel: null
        },
        view: function(view) {
            view.content.push({
                name: 'source',
                type: 'nx.graphic.Text',
                props: {
                    'class': 'sourcelabel',
                    'alignment-baseline': 'text-after-edge',
                    'text-anchor': 'start'
                }
            }, {
                name: 'target',
                type: 'nx.graphic.Text',
                props: {
                    'class': 'targetlabel',
                    'alignment-baseline': 'text-after-edge',
                    'text-anchor': 'end'
                }
            });
            return view;
        },
        methods: {
            update: function() {
                this.inherited();
                var el, point;
                var line = this.line();
                var angle = line.angle();
                var stageScale = this.stageScale();
                line = line.pad(18 * stageScale, 18 * stageScale);
                if (this.sourcelabel()) {
                    el = this.view('source');
                    point = line.start;
                    el.set('x', point.x);
                    el.set('y', point.y);
                    el.set('text', this.sourcelabel());
                    el.set('transform', 'rotate(' + angle + ' ' + point.x + ',' + point.y + ')');
                    el.setStyle('font-size', 8 * stageScale);
                }
                if (this.targetlabel()) {
                    el = this.view('target');
                    point = line.end;
                    el.set('x', point.x);
                    el.set('y', point.y);
                    el.set('text', this.targetlabel());
                    el.set('transform', 'rotate(' + angle + ' ' + point.x + ',' + point.y + ')');
                    el.setStyle('font-size', 8 * stageScale);
                }
            }
        }
    });

    // Initialize topology
    var topo = new nx.graphic.Topology({
        width: 1500,
        height:700,
        dataProcessor: 'force',
        identityKey: 'id',
        nodeConfig: {
            label: 'model.name',
            iconType: 'model.icon',
        },
        linkConfig: {
            linkType: 'parallel',
            sourcelabel: 'model.srcIfName',
            targetlabel: 'model.tgtIfName',
            style: function(model) {
                if (model._data.is_dead === 'yes') {
                    return { 'stroke-dasharray': '5' };
                }
            },
            color: function(model) {
                if (model._data.is_dead === 'yes') {
                    return '#E40039';
                }
                if (model._data.is_new === 'yes') {
                    return '#148D09';
                }
            }
        },
        showIcon: true,
        linkInstanceClass: 'CustomLinkClass' // Use extended link class version with interface labels enabled
    });

    var Shell = nx.define(nx.ui.Application, {
        methods: {
            start: function () {
                topo.data(topologyData);
                topo.attach(this);
            }
        }
    });

    var shell = new Shell();
    shell.start();
})(nx);
