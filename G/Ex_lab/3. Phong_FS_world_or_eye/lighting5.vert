#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec3 color;
layout (location = 3) in vec2 texCoord;

out vec3 NE;
out vec3 VE;
out vec3 LE;

out vec3 NW;
out vec3 VW;
out vec3 LW;

uniform mat4 modelViewProjectionMatrix;
uniform mat4 modelViewMatrixInverse;
uniform mat4 modelViewMatrix;
uniform mat3 normalMatrix;

uniform vec4 lightPosition;


void main()
{
//eye
    vec3 P = (modelViewMatrix * vec4(vertex, 1)).xyz;
    NE = normalMatrix * normal;
    VE = -P;
    LE = lightPosition.xyz - P;
    
//word
    NW = normal;
    VW = (modelViewMatrixInverse * vec4(0,0,0,1)).xyz - vertex;
    LW = (modelViewMatrixInverse * lightPosition).xyz -vertex; 
    
    gl_Position = modelViewProjectionMatrix * vec4(vertex, 1.0);
}
