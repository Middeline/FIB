#version 330 core
        
layout(triangles) in;
layout(triangle_strip, max_vertices = 36) out;

in vec4 vfrontColor[];
out vec4 gfrontColor;

uniform mat4 modelViewProjectionMatrix;
uniform vec3 boundingBoxMin;
uniform vec3 boundingBoxMax;

void main( void )
{
    if (gl_PrimitiveIDIn == 0) {
        float R = (length(boundingBoxMax - boundingBoxMin))/2.0;
        vec3 C = (boundingBoxMax + boundingBoxMin)/2.0;

        vec4 cian = vec4(0, 1, 1, 1);
        vec4 pos;

        gfrontColor = cian;
        pos = vec4( C.x - R, boundingBoxMin.y - 0.01, C.z + R, 1);
        gl_Position = modelViewProjectionMatrix * pos;
        EmitVertex();

        gfrontColor = cian;
        pos = vec4( C.x - R, boundingBoxMin.y - 0.01, C.z - R, 1);
        gl_Position = modelViewProjectionMatrix * pos;
        EmitVertex();

        gfrontColor = cian;
        pos = vec4( C.x + R, boundingBoxMin.y - 0.01, C.z + R, 1);
        gl_Position = modelViewProjectionMatrix * pos;
        EmitVertex();
    
        gfrontColor = cian;
        pos = vec4( C.x + R, boundingBoxMin.y - 0.01, C.z - R, 1);
        gl_Position = modelViewProjectionMatrix * pos;
        EmitVertex();

        EmitVertex();

        EndPrimitive();
     }

	for( int i = 0 ; i < 3 ; i++ )
	{
		gfrontColor = vfrontColor[i];
		gl_Position = modelViewProjectionMatrix * gl_in[i].gl_Position;
		EmitVertex();
	}
    EndPrimitive();

    for (int i=0; i<3; ++i){
        gfrontColor = vec4(0.);
        vec4 P = gl_in[i].gl_Position;
        P.y = boundingBoxMin.y;
        gl_Position = modelViewProjectionMatrix * P;
        EmitVertex();
    }
    EndPrimitive();
}
