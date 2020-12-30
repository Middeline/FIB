#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 2) in vec3 color;

out vec4 frontColor;

uniform mat4 modelViewProjectionMatrix;

uniform float time;


void main()
{
    float alpha = 0.4 * vertex.y * sin(time);
    
    mat3 rotacioY = mat3 (
        vec3(cos(alpha), 0, sin(alpha)), 
        vec3(0, 1, 0), 
        vec3(-sin(alpha), 0, cos(alpha)));
     
    vec3 V = rotacioY * vertex;
    
    frontColor = vec4(color,1.0);
    
    gl_Position = modelViewProjectionMatrix * vec4(V, 1.0);
}
 
