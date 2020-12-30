#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec4 frontColor;
out vec2 vtexCoord;

uniform float amplitude=0.1;
uniform float freq = 1; // expressada en Hz

float pi2 =   acos(-1.0) * 2;

uniform mat4 modelViewProjectionMatrix;
uniform mat3 normalMatrix;

uniform float time;

void main()
{
    vec3 N = normalize(normalMatrix * normal);
    
    //animate-vertices1
    //vec3 V = vertex + normal * amplitude * sin(pi2 * freq * time);
    
    //animate-vertices2
    vec3 V = vertex + normal * amplitude * sin(pi2 * freq * time + pi2 * freq * texCoord.x);
    
    frontColor = vec4(vec3(N.z), 1);
    gl_Position = modelViewProjectionMatrix * vec4(V, 1.0);
}
