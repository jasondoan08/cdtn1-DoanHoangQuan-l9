<mxfile host="app.diagrams.net">
  <diagram name="Trang-1" id="ZzePuPSEVnVJjk7R20Au">
    <mxGraphModel dx="860" dy="1642" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="x3IdI3yIwJpPPJKW-AOi-1" parent="1" style="rounded=0;whiteSpace=wrap;html=1;labelPosition=center;verticalLabelPosition=top;align=center;verticalAlign=bottom;fontSize=16;" value="Hệ thông phân loại lỗi bảo hành AI" vertex="1">
          <mxGeometry height="280" width="540" x="150" as="geometry" />
        </mxCell>
        <mxCell id="x3IdI3yIwJpPPJKW-AOi-2" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;" value="Nhân viên tiếp nhận" vertex="1">
          <mxGeometry height="60" width="30" x="40" y="90" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-9" edge="1" parent="1" source="x3IdI3yIwJpPPJKW-AOi-4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;dashed=1;" target="x3IdI3yIwJpPPJKW-AOi-5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-10" connectable="0" parent="A8Czvj3LrHlriOAP3Ytl-9" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="&amp;lt;&amp;lt;include&amp;gt;&amp;gt;" vertex="1">
          <mxGeometry relative="1" x="-0.2444" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="x3IdI3yIwJpPPJKW-AOi-4" parent="1" style="ellipse;whiteSpace=wrap;html=1;shapeInside=1;" value="Tạo phiếu bảo hành mới" vertex="1">
          <mxGeometry height="80" width="120" x="160" as="geometry" />
        </mxCell>
        <mxCell id="x3IdI3yIwJpPPJKW-AOi-5" parent="1" style="ellipse;whiteSpace=wrap;html=1;shapeInside=1;" value="Dự đoán nhóm sự cố tự động" vertex="1">
          <mxGeometry height="80" width="120" x="290" y="60" as="geometry" />
        </mxCell>
        <mxCell id="x3IdI3yIwJpPPJKW-AOi-6" parent="1" style="ellipse;whiteSpace=wrap;html=1;shapeInside=1;" value="Hiệu chỉnh kết quả dự đoán&amp;nbsp;" vertex="1">
          <mxGeometry height="80" width="120" x="160" y="200" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-4" parent="1" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;" value="Đường liền: Tương tác trực tiếp. Đường nét đứt: Bắt bược đi kèm" vertex="1">
          <mxGeometry height="110" width="80" x="30" y="270" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-11" parent="1" style="ellipse;whiteSpace=wrap;html=1;shapeInside=1;" value="Trích xuất dữ liệu huấn luyện" vertex="1">
          <mxGeometry height="80" width="120" x="294" y="150" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-12" parent="1" style="ellipse;whiteSpace=wrap;html=1;shapeInside=1;" value="Xem báo cáo hiệu năng AI" vertex="1">
          <mxGeometry height="80" width="120" x="160" y="100" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-23" edge="1" parent="1" source="A8Czvj3LrHlriOAP3Ytl-18" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;endArrow=none;endFill=0;" target="x3IdI3yIwJpPPJKW-AOi-6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-18" parent="1" style="shape=waypoint;sketch=0;fillStyle=solid;size=6;pointerEvents=1;points=[];fillColor=none;resizable=0;rotatable=0;perimeter=centerPerimeter;snapToPoint=1;" value="" vertex="1">
          <mxGeometry height="20" width="20" x="60" y="140" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-27" parent="1" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;" value="Quản trị viên AI" vertex="1">
          <mxGeometry height="60" width="30" x="45" y="-50" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-33" edge="1" parent="1" source="A8Czvj3LrHlriOAP3Ytl-30" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;endArrow=none;endFill=0;" target="A8Czvj3LrHlriOAP3Ytl-12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-30" parent="1" style="shape=waypoint;sketch=0;fillStyle=solid;size=6;pointerEvents=1;points=[];fillColor=none;resizable=0;rotatable=0;perimeter=centerPerimeter;snapToPoint=1;" value="" vertex="1">
          <mxGeometry height="20" width="20" x="60" y="-40" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-31" parent="1" style="shape=waypoint;sketch=0;fillStyle=solid;size=6;pointerEvents=1;points=[];fillColor=none;resizable=0;rotatable=0;perimeter=centerPerimeter;snapToPoint=1;" value="" vertex="1">
          <mxGeometry height="20" width="20" x="60" y="100" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-35" edge="1" parent="1" source="A8Czvj3LrHlriOAP3Ytl-32" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;endArrow=none;endFill=0;" target="A8Czvj3LrHlriOAP3Ytl-11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="A8Czvj3LrHlriOAP3Ytl-32" parent="1" style="shape=waypoint;sketch=0;fillStyle=solid;size=6;pointerEvents=1;points=[];fillColor=none;resizable=0;rotatable=0;perimeter=centerPerimeter;snapToPoint=1;" value="" vertex="1">
          <mxGeometry height="20" width="20" x="30" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
