
#version 330 core
        
layout(triangles) in;
layout(triangle_strip, max_vertices = 36) out;

in vec4 vfrontColor[];
out vec4 gfrontColor;

uniform mat4 modelViewProjectionMatrix;
uniform float step = 0.2;

vec4 center = vec4(round(((gl_in[0].gl_Position.xyz + gl_in[1].gl_Position.xyz + gl_in[2].gl_Position.xyz)/3.0) / step) * step, 0.0);

void emitCara(vec4 v1, vec4 v2, vec4 v3, vec4 v4, vec4 color) {
	gfrontColor = color;
	gl_Position = modelViewProjectionMatrix * (center + v1);
	EmitVertex();
	gl_Position = modelViewProjectionMatrix * (center + v2);
	EmitVertex();
	gl_Position = modelViewProjectionMatrix * (center + v3);
	EmitVertex();
	gl_Position = modelViewProjectionMatrix * (center + v4);
	EmitVertex();
	EndPrimitive();
}

void main( void )
{
	float s = step/2.0;
	
	vec4 gris = vec4(0.3, .3, .3, 1);
	
	vec4 v1 = vec4(s, s, s, 1.0); vec4 v2 = vec4(-s, s, s, 1.0);
	vec4 v3 = vec4(s, -s, s, 1.0); vec4 v4 = vec4(-s, -s, s, 1.0);
	vec4 v5 = vec4(s, s, -s, 1.0); vec4 v6 = vec4(-s, s, -s, 1.0); 
	vec4 v7 = vec4(s, -s, -s, 1.0); vec4 v8 = vec4(-s, -s, -s, 1.0);
	
	emitCara(v1, v2, v3, v4, gris);
	emitCara(v5, v6, v7, v8, gris);
	emitCara(v1, v3, v5, v7, gris);
	emitCara(v2, v4, v6, v8, gris);
	emitCara(v1, v2, v5, v6, gris);
	emitCara(v2, v3, v7, v8, gris);
}
