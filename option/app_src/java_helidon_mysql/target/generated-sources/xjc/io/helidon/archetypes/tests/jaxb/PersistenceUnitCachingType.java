//
// This file was generated by the Eclipse Implementation of JAXB, v3.0.0 
// See https://eclipse-ee4j.github.io/jaxb-ri 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2022.10.14 at 07:01:54 AM GMT 
//


package io.helidon.archetypes.tests.jaxb;

import jakarta.annotation.Generated;
import jakarta.xml.bind.annotation.XmlEnum;
import jakarta.xml.bind.annotation.XmlType;


/**
 * <p>Java class for persistence-unit-caching-type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <pre>
 * &lt;simpleType name="persistence-unit-caching-type"&gt;
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}token"&gt;
 *     &lt;enumeration value="ALL"/&gt;
 *     &lt;enumeration value="NONE"/&gt;
 *     &lt;enumeration value="ENABLE_SELECTIVE"/&gt;
 *     &lt;enumeration value="DISABLE_SELECTIVE"/&gt;
 *     &lt;enumeration value="UNSPECIFIED"/&gt;
 *   &lt;/restriction&gt;
 * &lt;/simpleType&gt;
 * </pre>
 * 
 */
@XmlType(name = "persistence-unit-caching-type")
@XmlEnum
@Generated(value = "com.sun.tools.xjc.Driver", comments = "JAXB RI v3.0.0", date = "2022-10-14T07:01:54+00:00")
public enum PersistenceUnitCachingType {

    ALL,
    NONE,
    ENABLE_SELECTIVE,
    DISABLE_SELECTIVE,
    UNSPECIFIED;

    public String value() {
        return name();
    }

    public static PersistenceUnitCachingType fromValue(String v) {
        return valueOf(v);
    }

}
