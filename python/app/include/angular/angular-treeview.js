/*
	@license Angular Treeview version 0.1.6
	ⓒ 2013 AHN JAE-HA http://github.com/eu81273/angular.treeview
	License: MIT


	[TREE attribute]
	angular-treeview: the treeview directive
	tree-id : each tree's unique id.
	tree-model : the tree model on $scope.
	node-id : each node's id
	node-label : each node's label
	node-children: each node's children

	<div
		data-angular-treeview="true"
		data-tree-id="tree"
		data-tree-model="roleList"
		data-node-id="roleId"
		data-node-label="roleName"
		data-node-children="children" >
	</div>
*/

(function ( angular ) {
	'use strict';

	angular.module( 'angularTreeview', [] ).directive( 'treeModel', ['$compile', function( $compile ) {
		return {
			restrict: 'A',
			link: function ( scope, element, attrs ) {
				//tree id
				var treeId = attrs.treeId;
			
				//tree model
				var treeModel = attrs.treeModel;

				//node id
				var nodeId = attrs.nodeId || 'id';

				//node label
				var nodeLabel = attrs.nodeLabel || 'label';

				//node desc
				var nodeDesc = attrs.nodeDesc || '';

				//children
				var nodeChildren = attrs.nodeChildren || 'children';

				//tree template
				/*var template =
					'<ul>' +
						'<li data-ng-repeat="node in ' + treeModel + '">' +
							'<i class="collapsed" data-ng-show="node.' + nodeChildren + '.length && node.collapsed" data-ng-click="' + treeId + '.selectNodeHead(node)"></i>' +
							'<i class="expanded" data-ng-show="node.' + nodeChildren + '.length && !node.collapsed" data-ng-click="' + treeId + '.selectNodeHead(node)"></i>' +
							'<i class="normal" data-ng-hide="node.' + nodeChildren + '.length"></i> ' +
							'<span data-ng-class="node.selected" data-ng-click="' + treeId + '.selectNodeLabel(node)">{{node.' + nodeLabel + '}}</span>' +
							'<div data-ng-hide="node.collapsed" data-tree-id="' + treeId + '" data-tree-model="node.' + nodeChildren + '" data-node-id=' + nodeId + ' data-node-label=' + nodeLabel + ' data-node-children=' + nodeChildren + '></div>' +
						'</li>' +
					'</ul>';*/
				var template =
					'<ul>' +
						'<li data-ng-repeat="node in ' + treeModel + '">' +
							'<div class="contact_item_left" lazy-container="resources/userDefault.png">' +
								// '<div ng-if="node.LEAF == 2">' +
								'<div ng-if="node.OTYPE != 3">' +
									'<i data-ng-click="unSelectKey[node.' + nodeId + '] || ' + treeId + '.selectNodeLabel(node, $event, true)" class="select_all_mask" ng-class="{web_cochat_choose_green_radio: selectKey[node.' + nodeId + '], web_cochat_choose_gray_radio: unSelectKey[node.' + nodeId + '], web_cochat_choose_wireframe_radio: !selectKey[node.' + nodeId + '] && !unSelectKey[node.' + nodeId + '] && !hideSelectBox[node.' + nodeId + '], web_cochat_choose_opacity: initSelectKey[node.' + nodeId + ']}"></i>' +
									'<div class="org_container" data-ng-click="unSelectKey[node.' + nodeId + '] || ' + treeId + '.selectNodeLabel(node, $event)">' +
										'<h4 class="nickname">' +
											'<span class="org_name">{{node.' + nodeLabel + '}}</span>' +
											'<i class="expand" data-ng-show="node.collapsed || node.collapsed == undefined" ng-class="{org_hideexpand:node.SUBDEPTCOUNT <=0 }"></i>' +
											'<i class="collapse" data-ng-show="!node.collapsed && node.collapsed != undefined"></i>' +
										'</h4>' +
									'</div>' +
								'</div>' +

								// '<div ng-if="node.LEAF == 1">' +
								'<div ng-if="node.OTYPE == 3" data-ng-click="unSelectKey[node.' + nodeId + '] || ' + treeId + '.selectNodeLabel(node, $event)">' +
									'<div class="opt_left" ng-if="!hideSelected">' +
										'<i ng-class="{web_cochat_choose_green_radio: selectKey[node.' + nodeId + '], web_cochat_choose_gray_radio: unSelectKey[node.' + nodeId + '], web_cochat_choose_wireframe_radio: !selectKey[node.' + nodeId + '] && !unSelectKey[node.' + nodeId + '], web_cochat_choose_opacity: initSelectKey[node.' + nodeId + ']}"></i>' +
									'</div>' +
                                    '<div class="avatar">' +
                                        //'<img class="img_left lazy" lazy-src="{{node.' + nodeId + ' | userIcon}}"/>' +
										'<div head-portrait user-code="node.' + nodeId + '" user-name="node.' + nodeLabel + '" img-width="34" img-height="34"></div>' +
                                    '</div>' +
                                    '<div class="info">' +
                                        '<h4><span class="nickname_left" ng-bind="node.' + nodeLabel + '"></span><span class="desc" ng-bind="node.' + nodeDesc + '"></span></h4>' +
                                    '</div>' +
                                '</div>' +
							'</div>' +
							'<div data-ng-hide="node.collapsed" data-tree-id="' + treeId + '" data-tree-model="node.' + nodeChildren + '" data-node-id=' + nodeId + ' data-node-label=' + nodeLabel + ' data-node-desc=' + nodeDesc + ' data-node-children=' + nodeChildren + '></div>' +
						'</li>' +
					'</ul>';


				//check tree id, tree model
				if( treeId && treeModel ) {

					//root node
					if( attrs.angularTreeview ) {
					
						//create tree object if not exists
						scope[treeId] = scope[treeId] || {};

						//if node head clicks,
						scope[treeId].selectNodeHead = scope[treeId].selectNodeHead || function( selectedNode ){

							//Collapse or Expand
							selectedNode.collapsed = !selectedNode.collapsed;
						};

						//if node label clicks,
						scope[treeId].selectNodeLabel = scope[treeId].selectNodeLabel || function( selectedNode ){

							//remove highlight from previous node
							if( scope[treeId].currentNode && scope[treeId].currentNode.selected ) {
								scope[treeId].currentNode.selected = undefined;
							}

							//set highlight to selected node
							selectedNode.selected = 'selected';

							//set currentNode
							scope[treeId].currentNode = selectedNode;
						};
					}

					//Rendering template.
					element.html('').append( $compile( template )( scope ) );
				}
			}
		};
	}]);
})( angular );
