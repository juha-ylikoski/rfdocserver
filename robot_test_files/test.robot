*** Settings ***
Documentation     Test resource file
...               Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed enim metus, aliquet lacinia nisi eget, posuere sagittis libero. Proin vitae lacus sagittis, vehicula est sit amet, aliquet urna. Morbi metus ante, elementum in eros quis, maximus rhoncus augue. Integer faucibus est non tortor tristique laoreet. Ut eleifend sollicitudin mi eget consectetur. Donec id lacus sit amet urna luctus auctor rutrum eget neque. Curabitur pulvinar consectetur erat, ut dignissim enim tincidunt ut. Ut vestibulum purus ac orci sodales, a ultricies magna convallis. Mauris velit mi, accumsan sit amet nibh in, interdum lobortis lorem. Quisque feugiat turpis venenatis elementum ultrices. Quisque dignissim finibus pharetra. Praesent non congue lorem.
...               Vivamus lobortis felis vel finibus interdum. Fusce a quam risus. Donec faucibus orci id odio rutrum rutrum. Donec et vestibulum lacus, non vulputate leo. Ut sit amet ligula urna. Donec ut enim ligula. Vivamus libero mi, convallis quis aliquam ac, rhoncus vel odio. Sed enim sem, semper eget sollicitudin fringilla, scelerisque commodo dui. Praesent est augue, suscipit ac dictum id, rhoncus et lacus.
Library           String

*** Variables ***
${FOO}            BAR

*** Keywords ***
Empty Keyword

Keyword With Documentation
    [Documentation]    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed enim metus, aliquet lacinia nisi eget, posuere sagittis libero. Proin vitae lacus sagittis, vehicula est sit amet, aliquet urna. Morbi metus ante, elementum in eros quis, maximus rhoncus augue. Integer faucibus est non tortor tristique laoreet. Ut eleifend sollicitudin mi eget consectetur. Donec id lacus sit amet urna luctus auctor rutrum eget neque. Curabitur pulvinar consectetur erat, ut dignissim enim tincidunt ut. Ut vestibulum purus ac orci sodales, a ultricies magna convallis. Mauris velit mi, accumsan sit amet nibh in, interdum lobortis lorem. Quisque feugiat turpis venenatis elementum ultrices. Quisque dignissim finibus pharetra. Praesent non congue lorem.
    ...    Vivamus lobortis felis vel finibus interdum. Fusce a quam risus. Donec faucibus orci id odio rutrum rutrum. Donec et vestibulum lacus, non vulputate leo. Ut sit amet ligula urna. Donec ut enim ligula. Vivamus libero mi, convallis quis aliquam ac, rhoncus vel odio. Sed enim sem, semper eget sollicitudin fringilla, scelerisque commodo dui. Praesent est augue, suscipit ac dictum id, rhoncus et lacus.

Keyword With Tag
    [Tags]    Foo    Bar

Keyword With Arguments
    [Arguments]    ${Foo}    ${Bar}    ${Foo_Bar}=Foo_Bar

Keyword With Return
    [Return]    Foo

Keyword With All
    [Documentation]    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed enim metus, aliquet lacinia nisi eget, posuere sagittis libero. Proin vitae lacus sagittis, vehicula est sit amet, aliquet urna. Morbi metus ante, elementum in eros quis, maximus rhoncus augue. Integer faucibus est non tortor tristique laoreet. Ut eleifend sollicitudin mi eget consectetur. Donec id lacus sit amet urna luctus auctor rutrum eget neque. Curabitur pulvinar consectetur erat, ut dignissim enim tincidunt ut. Ut vestibulum purus ac orci sodales, a ultricies magna convallis. Mauris velit mi, accumsan sit amet nibh in, interdum lobortis lorem. Quisque feugiat turpis venenatis elementum ultrices. Quisque dignissim finibus pharetra. Praesent non congue lorem.
    ...    Vivamus lobortis felis vel finibus interdum. Fusce a quam risus. Donec faucibus orci id odio rutrum rutrum. Donec et vestibulum lacus, non vulputate leo. Ut sit amet ligula urna. Donec ut enim ligula. Vivamus libero mi, convallis quis aliquam ac, rhoncus vel odio. Sed enim sem, semper eget sollicitudin fringilla, scelerisque commodo dui. Praesent est augue, suscipit ac dictum id, rhoncus et lacus.
    [Tags]    Foo    Bar
    [Arguments]    ${Foo}    ${Bar}    ${Foo_Bar}=Foo_Bar
    [Return]    Foo

Filler1

Filler2

Filler3

Filler4

Filler5

Filler6

Filler7

Filler8

Filler9

Filler10

Filler12

Filler13

Filler11

Filler41

Filler51

Filler61

Filler71

Filler81

Filler91

Filler101

Filler121

Filler131

Filler111

Filler211

Filler311

Filler411

Filler511

Filler611

Filler711

Filler811

Filler911

Filler1011

Filler1211

Filler1111

Filler1311

Filler4111

Filler5111

Filler6111

Filler7111

Filler8111

Filler9111

Filler10111

Filler11111

Filler12111

Filler13111

