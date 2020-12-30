#version 330 core
        
layout(triangles) in;
layout(triangle_strip, max_vertices = 36) out;

in vec4 vfrontColor[];
out vec4 gfrontColor;

const float speed = 1.2;

uniform mat4 modelViewProjectionMatrix;
uniform float time;

in vec3 vN[];


void main( void )
{
	
    vec3 n = (vN[0] + vN[1] + vN[2])/3.0;
    vec3 T = speed*time*n;

    for( int i = 0 ; i < 3 ; i++ ) {
	 gfrontColor = vfrontColor[i];
     vec4 pos = gl_in[i].gl_Position;
     pos += vec4(T, 0.0);
      
     gl_Position = modelViewProjectionMatrix * pos;
     EmitVertex(); 
    }
    EndPrimitive();
    
}
